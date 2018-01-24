import cv2
import numpy as np

img = cv2.imread('hzxc2.jpg',1)

# 分离图像 得到BGR三个通道的图像分量
b,g,r = cv2.split(img)

# 显示原图和三个通道
cv2.namedWindow('Source Image')
cv2.namedWindow('Blue Channel')
cv2.namedWindow('Green Channel')
cv2.namedWindow('Red Channel')
cv2.imshow('Source Image', img)
cv2.imshow('Blue Channel', b)
cv2.imshow('Green Channel', g)
cv2.imshow('Red Channel', r)

# 转换为HSV色彩空间
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 分离HSV三通道
h,s,v = cv2.split(hsv)
# 显示原图和三个通道
cv2.namedWindow('HSV')
cv2.namedWindow('H')
cv2.namedWindow('S')
cv2.namedWindow('V')
cv2.imshow('HSV', hsv)
cv2.imshow('H', h)
cv2.imshow('S', s)
cv2.imshow('V', v)
cv2.waitKey(0)
cv2.destroyAllWindows()
