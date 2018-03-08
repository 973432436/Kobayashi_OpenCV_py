import cv2
import numpy as np

img = cv2.imread('E:\\OpenCV\\py_version\\demo\\venv\\Picture\\duolaameng.jpeg')
# 图像预处理
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binImg = cv2.threshold(grayImg, 100, 255, cv2.THRESH_BINARY)
# 寻找轮廓
_, contours, hierarchy = cv2.findContours(binImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# 画出轮廓
cv2.drawContours(img, contours, 1, (0, 200, 0), 2)
cv2.imshow('Contours Image', img)
print(contours[1].shape)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('Contours.jpg', img)