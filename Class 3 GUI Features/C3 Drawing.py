import numpy as np
import cv2

# 创建一张黑色三通道图像
img = np.zeros((512, 512, 3), np.uint8)
# 画直线
img = cv2.line(img, (0, 0), (250, 250), (0, 0, 255), 2)
# 画矩形
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# 画圆形
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
# 画椭圆
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
# 放置字符
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

# 显示并保存图像
cv2.imshow('img', img)
cv2.imwrite('Drawing Image.jpg', img)

cv2.waitKey(0)

cv2.destroyAllWindows()