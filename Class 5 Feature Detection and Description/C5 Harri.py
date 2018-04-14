import cv2
import numpy as np

img = cv2.imread('mavic air.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayImg = np.float32(grayImg)
harriImg = cv2.cornerHarris(grayImg, 2, 3, 0.04)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
harriImgD = cv2.dilate(harriImg, kernel)
img[harriImgD > 0.05*harriImgD.max()] = [0, 0, 255]
cv2.imshow('Harri', harriImgD)
cv2.imshow('Output', img)

cv2.waitKey()
cv2.destroyAllWindows()
