import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('nanji1.PNG')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', grayImg)
# 灰度图像的直方图
grayHist = cv2.calcHist([grayImg], [0], None, [256], [0, 256])
plt.subplot(321), plt.plot(grayHist)
# 彩色图像生成直方图
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    bgrHist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.subplot(322), plt.plot(bgrHist, color=col)
    plt.xlim([0, 256])
# 掩膜处理
# 创建掩膜
mask = np.zeros(grayImg.shape[:2], np.uint8)
mask[200:500, 300:600] = 255
masked_img = cv2.bitwise_and(grayImg, grayImg, mask=mask)

# 分别计算不带掩膜和带掩膜的直方图数据
hist_full = cv2.calcHist([grayImg], [0], None, [256], [0, 256])
hist_mask = cv2.calcHist([grayImg], [0], mask, [256], [0, 256])

plt.subplot(323), plt.imshow(grayImg, 'gray')
plt.subplot(324), plt.imshow(mask, 'gray')
plt.subplot(325), plt.imshow(masked_img, 'gray')
plt.subplot(326), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0, 256])

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()