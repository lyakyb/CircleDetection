import cv2
import numpy as np

def emptyFunc(dummy):
    pass


finalWindow = 'Final'
cv2.namedWindow(finalWindow)
mb = 'mb'
gb = 'gb'
ce = 'ce'
cv2.createTrackbar(mb, finalWindow, 15, 55, emptyFunc)
cv2.createTrackbar(gb, finalWindow, 5, 21, emptyFunc)
cv2.createTrackbar(ce, finalWindow, 110, 300, emptyFunc)

orgImg = cv2.imread('TestImages/1.JPG')
orgImg = cv2.resize(orgImg, (720, 540))



while True:
    mbVal = cv2.getTrackbarPos(mb, finalWindow)
    gbVal = cv2.getTrackbarPos(gb, finalWindow)
    ceVal = cv2.getTrackbarPos(ce, finalWindow)

    orgImgCopy = orgImg.copy()


    if mbVal % 2 == 0:
        mbVal += 1
    if gbVal % 2 == 0:
        gbVal += 1
    try:
        medianImg = cv2.medianBlur(orgImg, mbVal)
        gaussImg = cv2.GaussianBlur(medianImg, (gbVal, gbVal), 0)

        print('cur mb: ' + str(mbVal))
        print('cur gb: ' + str(gbVal))

        canImg = cv2.Canny(gaussImg, ceVal / 2, ceVal)
        gray = cv2.cvtColor(gaussImg, cv2.COLOR_BGR2GRAY)

        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 30, param1=ceVal, param2=30, minRadius=10, maxRadius=300)
        circles = np.uint16(np.around(circles))

        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(orgImgCopy,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(orgImgCopy,(i[0],i[1]),2,(0,0,255),3)
    except AttributeError as e:
        print('------------------------------------')
        print('Attribute Exception: '+ str(e.args))
        print('mb: ' + str(mbVal))
        print('gb: ' + str(gbVal))
        print('------------------------------------')
    #show the image
    cv2.imshow(finalWindow, orgImgCopy)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
