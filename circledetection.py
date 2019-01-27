import cv2
import numpy as np

def emptyFunc(dummy):
    pass

# for x in range (0, 7):
orgImg = cv2.imread('TestImages/1.JPG')
orgImg = cv2.resize(orgImg, (720,540))
orgImgCopy = orgImg.copy()
cv2.imshow('Original Input', orgImg)

medianImg = cv2.medianBlur(orgImg, 15)
cv2.imshow('Median Blurred', medianImg)

gaussImg = cv2.GaussianBlur(medianImg, (5,5),0)
cv2.imshow('Gaussian Blurred', gaussImg)

canVal = 110

canImg = cv2.Canny(gaussImg, canVal / 2, canVal)
cv2.imshow('canny', canImg)

gray = cv2.cvtColor(gaussImg, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 30, param1=canVal, param2=30, minRadius=10, maxRadius=300)
circles = np.uint16(np.around(circles))

# if circles is not None:
	# #draw boundary on the circle (contour-ish looking)
	# for circle in circles:
    #     for (x, y, r) in circle:
	# 	#the x,y is probably what we want to deal with for figuring out the distance from the ball and etc.
	# 	      cv2.circle(orgImgCopy, (int(x), int(y)), int(r), (0,0,255), 2)

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(orgImgCopy,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(orgImgCopy,(i[0],i[1]),2,(0,0,255),3)

#show the image
cv2.imshow('Final', orgImgCopy)
mb = 'mb'
gb = 'gb'
ce = 'ce'
cv2.createTrackbar(mb,'Final',0,99,emptyFunc)
cv2.createTrackbar(gb,'Final',0,50,emptyFunc)
cv2.createTrackbar(ce,'Final',0,300,emptyFunc)

cv2.waitKey(0)
# if cv2.waitKey(1) & 0xFF == ord('q'):
#     break
