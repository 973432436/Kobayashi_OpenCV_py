import cv2
import numpy as np

img = cv2.imread('IMG_8257.JPG',1)

# 确定ROI区域
ROI = img[20:300, 220:520]

# 分别显示原图和ROI区域
cv2.namedWindow('SRC')
cv2.namedWindow('ROI')
cv2.imshow('SRC', img)
cv2.imshow('ROI', ROI)

cv2.waitKey(0)
cv2.destroyAllWindows()
