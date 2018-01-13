import numpy as np
import cv2

# 初始化摄像头
cap = cv2.VideoCapture(0)

# 用循环不断获取当前帧 处理后显示出来
while True:
    if cap.isOpened():
#       捕获当前帧
        ret,frame = cap.read()
#       显示图像
        cv2.imshow('Camera', frame)

#   结束帧捕获的条件
#   等待100ms 即帧频为10fps
    if cv2.waitKey(100) & 0xFF is ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
