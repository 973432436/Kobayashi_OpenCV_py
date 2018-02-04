import cv2
import numpy as np

def blurTrackbar(x):
	pass

def GaussianBlurTarckbar(x):
	pass

img = cv2.imread('E:\\OpenCV\\py_version\\demo\\venv\\Picture\\IMG_8872.jpg')

# 为方便显示 我们将窗口适当缩小
cv2.namedWindow('Blur',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Blur', 480, 640)
cv2.namedWindow('Gaussian Blur',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Gaussian Blur', 480, 640)

cv2.createTrackbar('ksize', 'Blur', 1, 30, blurTrackbar)
cv2.createTrackbar('ksize', 'Gaussian Blur', 1, 30, GaussianBlurTarckbar)

while(True):
	blurKsize = cv2.getTrackbarPos('ksize', 'Blur')
	GaussianKsize = cv2.getTrackbarPos('ksize', 'Gaussian Blur')
#   采用长宽相同的核
	blurImg = cv2.blur(img, (blurKsize, blurKsize))
#   高斯滤波中 核的尺寸需为正奇数
	if GaussianKsize % 2 is 0:
		GaussianKsize = GaussianKsize + 1
#   采用长宽相同的核
	gauBlurImg = cv2.GaussianBlur(img, (GaussianKsize, GaussianKsize), 0, None, 0)
	
	cv2.imshow('Blur', blurImg)
	cv2.imshow('Gaussian Blur', gauBlurImg)
	
	if cv2.waitKey(1) & 0xFF is ord('q'):
		break

cv2.destroyAllWindows()
