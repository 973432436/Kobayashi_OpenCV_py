import cv2
import numpy as np

img = cv2.imread('hand1.jpg')

blurImg = cv2.GaussianBlur(img, (9, 9), 0)
# 获得纯边缘
cannyImg = cv2.Canny(blurImg, 50, 130)
# 取反
cannyImg_inv = cv2.bitwise_not(cannyImg)
# 转换成BGR空间
cannyImg_mask = cv2.cvtColor(cannyImg_inv, cv2.COLOR_GRAY2BGR)
# 处理原图
cannySrcImg = cv2.bitwise_and(img, cannyImg_mask)
# 处理掩膜
cannyImg_mask = cv2.bitwise_not(cannyImg_mask)
# 改变掩膜中边缘的颜色 这里显示红色
cannyImg_mask[:, :, [0, 1]] = 0
# 掩膜与处理后的原图叠加
cannyImg_target = cv2.add(cannySrcImg, cannyImg_mask)

cv2.imshow('Canny', cannyImg_target)

cv2.waitKey()
cv2.destroyAllWindows()
