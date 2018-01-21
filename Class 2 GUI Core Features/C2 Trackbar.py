import cv2
import numpy as np
# 滑动条回调函数 这里啥也不做（才怪）
def nothing(x):
    pass

# 创建画布
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# 创建并“激活”滑动条
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# 用滑动条做一个二值开关
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

#   获取滑动条当前值
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')
#   混合BGR通道
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()