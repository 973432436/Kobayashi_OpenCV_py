import cv2
import numpy as np

img = cv2.imread('E:\\OpenCV\\py_version\\demo\\venv\\Picture\\Mavic Air Fly.jpeg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create(400, upright=True)
kp, des = surf.detectAndCompute(grayImg, None)

img2 = cv2.drawKeypoints(img, kp, None, (0, 255, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SURF Image', img2)
cv2.imwrite('surfDetect.jpg', img2)
cv2.waitKey()
cv2.destroyAllWindows()
