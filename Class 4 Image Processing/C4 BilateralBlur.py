import cv2
import numpy as np

img = cv2.imread('IMG_8872.jpg')

# 为方便显示 我们将窗口适当缩小
cv2.namedWindow('Bilateral Blur', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Bilateral Blur', 480, 640)

BilateralBlurImg = cv2.bilateralFilter(img, 25, 25*2, 25/2)
	
cv2.imshow('Bilateral Blur', BilateralBlurImg)
	
cv2.waitKey()

cv2.destroyAllWindows()
