import cv2
import numpy as np


def medianBlurTrackbar(x):
	pass

img = cv2.imread('IMG_8872.jpg')

# 为方便显示 我们将窗口适当缩小
cv2.namedWindow('Median Blur', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Median Blur', 480, 640)

cv2.createTrackbar('ksize', 'Median Blur', 1, 30, medianBlurTrackbar)

while (True):
	MedianKsize = cv2.getTrackbarPos('ksize', 'Median Blur')

	if MedianKsize % 2 is 0:
		MedianKsize = MedianKsize + 1
	#   采用长宽相同的核
	MedianBlurImg = cv2.medianBlur(img, MedianKsize)

	cv2.imshow('Median Blur', MedianBlurImg)
	cv2.imwrite('MedianBlurDemo.jpg', MedianBlurImg)
	
	if cv2.waitKey(1) & 0xFF is ord('q'):
		break

cv2.destroyAllWindows()
