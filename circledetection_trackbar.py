import cv2
import numpy as np

def emptyFunc(dummy):
    pass


finalWindow = 'Final'
cv2.namedWindow(finalWindow)
md = 'Minimum Distance'
cu = 'Canny Upper'
p2 = 'Param 2'
mr = 'Minimum Radius'
mxr = 'Maximum Radius'
cv2.createTrackbar(md, finalWindow, 50, 300, emptyFunc)
cv2.createTrackbar(cu, finalWindow, 100, 255, emptyFunc)
cv2.createTrackbar(p2, finalWindow, 100, 255, emptyFunc)
cv2.createTrackbar(mr, finalWindow, 100, 300, emptyFunc)
cv2.createTrackbar(mxr, finalWindow, 200, 500, emptyFunc)

orgImg = cv2.imread('TestImages/1.JPG')
orgImg = cv2.resize(orgImg, (720, 540))

while True:
    mdVal = cv2.getTrackbarPos(md, finalWindow)
    cuVal = cv2.getTrackbarPos(cu, finalWindow)
    p2Val = cv2.getTrackbarPos(p2, finalWindow)
    mrVal = cv2.getTrackbarPos(mr, finalWindow)
    mxrVal = cv2.getTrackbarPos(mxr, finalWindow)

    orgImgCopy = orgImg.copy()
    try:
        medianImg = cv2.medianBlur(orgImg, 5)
        gaussImg = cv2.GaussianBlur(medianImg, (5, 5), 0)

        canImg = cv2.Canny(gaussImg, 75, 150)
        gray = cv2.cvtColor(gaussImg, cv2.COLOR_BGR2GRAY)

        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, mdVal, param1=cuVal, param2=p2Val, minRadius=mrVal, maxRadius=mxrVal)
        circles = np.uint16(np.around(circles))

        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(orgImgCopy,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(orgImgCopy,(i[0],i[1]),2,(0,0,255),3)
    except AttributeError as e:
        print(e)
    #show the image
    cv2.imshow(finalWindow, orgImgCopy)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
