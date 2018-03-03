import cv2
import numpy as np

img = cv2.imread('logo2.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circle = cv2.HoughCircles(grayImg, cv2.HOUGH_GRADIENT, 1, 50)

for c in circle:
	for x,y,r in c:
		cv2.circle(img, (x,y), r, (0, 0, 0), 2)

cv2.imshow('Circle', img)

cv2.waitKey()
cv2.destroyAllWindows()