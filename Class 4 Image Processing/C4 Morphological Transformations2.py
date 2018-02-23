import cv2
import numpy as np
from managers import CaptureManager,WindowManager

img = cv2.imread('E:\\OpenCV\\py_version\\demo\\venv\\Picture\\jjdbf2.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
openImg = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closeImg = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradImg = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('OpenImg', openImg)
cv2.imshow('CloseImg', closeImg)
cv2.imshow('GradientImg', gradImg)

cv2.imwrite('OpenImg.jpg', openImg)
cv2.imwrite('CloseImg.jpg', closeImg)
cv2.imwrite('GradientImg.jpg', gradImg)

cv2.waitKey()
cv2.destroyAllWindows()
