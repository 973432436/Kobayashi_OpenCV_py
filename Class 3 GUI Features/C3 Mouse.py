import cv2
import numpy as np

drawing = False # 若鼠标按下则为True
mode = True # 若为真则画矩形，否则画圆
ix,iy = -1,-1

# 鼠标回调函数
def draw_circle(event,x,y,flags,param):
#   全局变量，注意作用域
    global ix,iy,drawing,mode
#   事件：鼠标左键按下
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
#   事件：鼠标移动
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
#   事件：鼠标左键弹起
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

# 创建图像 也就是画布
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
# 设置鼠标回调函数
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
#   读取键码
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()