import cv2
import numpy as np

img1 = cv2.imread('mavic air.jpg')
img2 = cv2.imread('logo1.jpg')

# 创建ROI区域
rows1,cols1,channels1 = img1.shape
rows2,cols2,channels2 = img2.shape
roi = img1[rows1-rows2:rows1, cols1-cols2:cols1 ]

# 创建Logo的掩膜
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 170, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
cv2.namedWindow('mask_inv')
cv2.imshow('mask_inv', mask_inv)

# 在Mavic Air的ROI区域放上掩膜 即贴上"胶带"
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)

# 现在"刷上"颜色
img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)

# "撕掉胶带"
dst = cv2.add(img1_bg, img2_fg)
cv2.imwrite('merge.jpg', dst)
roi[:] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()