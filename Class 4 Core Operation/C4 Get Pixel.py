import cv2
import numpy as np

img = cv2.imread('IMG_8257.JPG', 1)
cv2.imshow('Image', img)

# 从矩阵里直接读取像素值
px1 = img[100, 10]
print('(100,10) BGR = ' + str(px1))
px2R = img[100, 10, 2]
print('(100,10) RED = ' + str(px2R))

# 从矩阵里直接修改像素值
px1 = [0, 0, 0]
img[100, 10] = px1
print('Modified directly ' + str(img[100, 10]))

# 使用numpy的方法
px3 = img.item(100, 20, 2)
print('Using numpy to get pixel(100,20)RED = ' + str(px3))
img.itemset((100, 20, 2), 120)
px3 = img.item(100, 20, 2)
print('Using numpy to modify pixel(100,20)RED = ' + str(px3))

# 获取图像属性
print(img.shape)
print(img.size)
print(img.dtype)

cv2.waitKey(0)
cv2.destroyAllWindows()
