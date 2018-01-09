import numpy as np
import cv2

print('Hello World.')
# 读取一张图片
img = cv2.imread("IMG_8257.JPG", 1)
# 显示一张图片
cv2.imshow('Image', img)
# 等待
cv2.waitKey(0)
# 销毁所有窗口以释放资源
cv2.destroyAllWindows()

