import cv2
import numpy as np

# 鼠标回调函数
def draw_circle(event,x,y,flags,param):
#   鼠标移动且按下Ctrl键
    if event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_CTRLKEY:
        print(param)
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# 创建画布
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
# “激活”回调函数 需要传递的参数为字符串'I am the param'
cv2.setMouseCallback('image',draw_circle,'I am the param')

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()