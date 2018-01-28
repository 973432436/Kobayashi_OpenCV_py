import numpy as np
import cv2
# 使用numpy新建两个图像矩阵
a = np.zeros((500,500),np.uint8)
b = np.ones((500,500),np.uint8)
# 以矩阵形式查看两个矩阵的内容
print(a)
print(b)
# numpy矩阵直接相加
c = a+b
# OpenCV提供的add方法
d = cv2.add(a,b)

cv2.namedWindow('b')
cv2.imshow('b',b)
b = b + 120
cv2.namedWindow('b+120')
cv2.imshow('b+120',b)
cv2.namedWindow('add')
cv2.imshow('add',d)
# 验证两种相加的方法得到的结果是否相同
print(c.all() == d.all())

cv2.waitKey()
cv2.destroyAllWindows()