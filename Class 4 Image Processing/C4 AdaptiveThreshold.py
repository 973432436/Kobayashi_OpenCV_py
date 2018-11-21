import cv2
import numpy as np

def threshBar(x):
	pass

img = cv2.imread('IMG_8881.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 适当缩小窗口
cv2.namedWindow('Thresh Window', cv2.WINDOW_NORMAL)
cv2.namedWindow('AdaptiveThresh Window', cv2.WINDOW_NORMAL)
cv2.namedWindow('BGR Thresh Window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Thresh Window', 640, 480)
cv2.resizeWindow('AdaptiveThresh Window', 640, 480)
cv2.resizeWindow('BGR Thresh Window', 640, 480)

ret, threshImg = cv2.threshold(grayImg, 122, 255, cv2.THRESH_BINARY)
ret, bgrThreshImg = cv2.threshold(img, 122, 255, cv2.THRESH_BINARY)
adaptiveThreshImg = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 49, 0)
cv2.imshow('AdaptiveThresh Window', adaptiveThreshImg)
cv2.imshow('Thresh Window', threshImg)
cv2.imshow('BGR Thresh Window', bgrThreshImg)

cv2.waitKey()
cv2.destroyAllWindows()
