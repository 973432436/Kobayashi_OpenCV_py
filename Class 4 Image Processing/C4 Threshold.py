import cv2
import numpy as np

def threshBar(x):
	pass

img = cv2.imread('E:\\OpenCV\\py_version\\demo\\venv\\Picture\\hzxc2.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Thresh Window')

cv2.createTrackbar('Thresh', 'Thresh Window', 0, 200, threshBar)

while(True):
	threshVal = cv2.getTrackbarPos('Thresh', 'Thresh Window')
	retval, threshImg = cv2.threshold(grayImg, threshVal, 255, cv2.THRESH_BINARY)
	cv2.imshow('Thresh Window', threshImg)
	if cv2.waitKey(1) & 0xFF is ord('q'):
		break

cv2.destroyAllWindows()
