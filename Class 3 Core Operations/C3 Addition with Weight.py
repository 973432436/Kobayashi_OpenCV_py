import cv2
import numpy as np

img1 = cv2.imread('m1.jpg')
img2 = cv2.imread('q1.jpg')

img3 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

cv2.namedWindow('img1')
cv2.namedWindow('img2')
cv2.namedWindow('img3')
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey()
cv2.destroyAllWindows()
