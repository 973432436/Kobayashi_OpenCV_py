import numpy as np
import cv2

#初始化摄像头
cap = cv2.VideoCapture(0)
index = 0
imgname = 0

#用循环不断获取当前帧 处理后显示出来
while True:
    index = index + 1
	#捕获当前帧
    ret,img = cap.read()
	
	#生成灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#阈值化处理 生成二值图像
    ret1,binary = cv2.threshold(gray, 160, 170, cv2.THRESH_BINARY)
	#对二值图像模糊处理
    bl = cv2.blur(binary, (3, 3))

	#创建两个窗口
    cv2.namedWindow('Binary')
    cv2.namedWindow('BGR')

	#显示图像
    cv2.imshow('Binary', bl)
    cv2.imshow('BGR',img)
	#每5秒保存一张截图
    if index == 50:
        imgname = imgname + 1
        if imgname >= 50:
            imgname = 0
		#文件名字符串拼接
        fname = str(imgname) + '.jpg'
		#写入截图
        cv2.imwrite(fname, img)
        index = 0
	#结束帧捕获的条件
	#等待100ms 即帧频为10fps
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

#释放资源
cap.release()
cv2.destroyAllWindows()
