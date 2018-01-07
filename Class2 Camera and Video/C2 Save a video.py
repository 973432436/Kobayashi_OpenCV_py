import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# 设置编码格式
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# 定义输出对象及输出格式
out = cv2.VideoWriter('VideoDemo.avi', fourcc, 20.0, (640,480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
#		将当前帧写入输出对象
        out.write(frame)
#		显示当前帧
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF is ord('q'):
            break
    else:
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()