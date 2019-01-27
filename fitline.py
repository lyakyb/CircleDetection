import cv2
import numpy as np

testImg = cv2.imread('TestImages/cargo.jpg')
rszImg = cv2.resize(testImg, (720,540))

hsvMin = np.array([59,99,40])
hsvMax = np.array([94,255,255])
hsvImg = cv2.cvtColor(rszImg, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsvImg, hsvMin, hsvMax)
res = cv2.bitwise_and(hsvImg,hsvImg, mask= mask)


contours, hierarchy = cv2.findContours(mask, 1, 2)
for cnt in contours:
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(res,[box],0,(0,0,255),2)

    rows,cols = mask.shape[:2]
    [vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)

    print("vX: " + str(vx))
    print("vY: " + str(vy))
    print("x: " + str(x))
    print("y: " + str(y))
    print("lefty: " + str(lefty))
    print("righty: " +str(righty))

    cv2.circle(res,(vx,vy),5,(255,0,0),-1)
    cv2.circle(res,(x,y),5,(0,0,255),-1)
    cv2.line(res,(cols-1,righty),(0,lefty),(0,255,0),2)

cv2.imshow('mask',mask)
cv2.imshow('res',res)

cv2.waitKey(0)

# if cv2.waitKey(1) & 0xFF == ord('q'):
#     break
