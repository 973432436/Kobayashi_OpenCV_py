import cv2
import numpy as np

img = cv2.imread('tuoer.jpg',1)
print(img.shape)
# 确定ROI区域 这里是引用
ROI = img[200:399, 480:639]
# 这里是复制 注意引用和复制的区别
ROIR = np.copy(ROI)
# 在引用的ROI矩阵中画红色矩形框
cv2.rectangle(ROI,(0,0),(158,198),(0,0,255))
# 分别显示原图和ROI区域
cv2.namedWindow('SRC')
cv2.namedWindow('ROI')
cv2.imshow('SRC', img)
cv2.imshow('ROI', ROIR)
cv2.imwrite('tuoer_ROI.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
