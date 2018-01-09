import cv2
import numpy as np

img = cv2.imread('IMG_8257.JPG',1)

# 分离图像 得到BGR三个通道的图像分量
b,g,r = cv2.split(img)

cv2.namedWindow('Source Image')
cv2.namedWindow('Blue Channel')
cv2.namedWindow('Green Channel')
cv2.namedWindow('Red Channel')
cv2.namedWindow('New Red Channel')
cv2.namedWindow('New Image')

# 显示原图和三个通道
cv2.imshow('Source Image', img)
cv2.imshow('Blue Channel', b)
cv2.imshow('Green Channel', g)
cv2.imshow('Red Channel', r)

# 在R通道中确定ROI区域 并修改ROI中所有像素的值
ROI = r[260:380, 30:120]
ROI = 255
r[260:380, 30:120] = ROI

# 显示修改后的R通道和它与BG通道合并后的新图
cv2.imshow('New Red Channel', r)
newImage = cv2.merge((b, g, r))
cv2.imshow('New Image', newImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
