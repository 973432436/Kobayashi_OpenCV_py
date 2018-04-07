import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('Jump.PNG')
img2 = cv2.imread('Jump2.PNG')
temp = cv2.imread('JumpTemp.PNG')
imgGray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
imgGrayCopy = imgGray.copy()
tempGray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
h, w = tempGray.shape

_, tempGray = cv2.threshold(tempGray, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('temp', tempGray)

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
	imgGray = imgGrayCopy.copy()
	method = eval(meth)
	res = cv2.matchTemplate(imgGray, tempGray, method)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		top_left = min_loc
	else:
		top_left = max_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)
	cv2.rectangle(imgGray, top_left, bottom_right, 0, 3)

	plt.subplot(121), plt.imshow(res, cmap='gray')
	plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
	plt.subplot(122), plt.imshow(imgGray, cmap='gray')
	plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
	plt.suptitle(meth)

	plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('JumpTempBin.jpg', tempGray)
