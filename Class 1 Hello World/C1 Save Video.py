import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# 定义fourecc代码
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# 创建VideoWriter对象
out = cv2.VideoWriter('VideoDemo.avi', fourcc, 20.0, (640,480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        out.write(frame)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF is ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()