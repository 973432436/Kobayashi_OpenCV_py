import numpy as np
import cv2

img = cv2.imread('mavic air.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cornerPoints = cv2.goodFeaturesToTrack(grayImg, 50, 0.01, 50)
cornerPoints = np.int0(cornerPoints)

for i in cornerPoints:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, [0, 0, 255], -1)

cv2.imshow('Shi-Tomasi', img)
cv2.waitKey()
