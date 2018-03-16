import cv2
import numpy as np

img = cv2.imread('duolaameng.jpeg')
# 图像预处理
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binImg = cv2.threshold(grayImg, 100, 255, cv2.THRESH_BINARY)
_, contours, hierarchy = cv2.findContours(binImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, 1, (0, 200, 0), 2)
x, y, w, h = cv2.boundingRect(contours[1])
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 200), 2)
# 计算凸包并画出
hull = cv2.convexHull(contours[1])
cv2.polylines(img, [hull], True, (255, 0, 0), 3)
'''
hull = cv2.convexHull(contours[1],returnPoints=False)
defects = cv2.convexityDefects(contours[1],hull)
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(contours[1][s])
    end = tuple(contours[1][e])
    far = tuple(contours[1][f])
    xs,ys = start[0]
    xe,ye = end[0]
    xf,yf = far[0]
    cv2.line(img,(xs,ys),(xe,ye),[255,0,0],3)
    cv2.circle(img,(xf,yf),4,[0,0,255],-1)
'''
cv2.imshow('Contours Image', img)

cv2.waitKey()
cv2.destroyAllWindows()
