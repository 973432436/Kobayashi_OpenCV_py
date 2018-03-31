import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('nanji1.PNG')
b, g, r = cv2.split(img)
imgRGB = cv2.merge((r, g, b))
equalHistImgBlue = cv2.equalizeHist(b)
equalHistImgRed = cv2.equalizeHist(r)
equalHistImgGreen = cv2.equalizeHist(g)
equalHistImg = cv2.merge((equalHistImgBlue, equalHistImgGreen, equalHistImgRed))
equalHistImgRGB = cv2.merge((equalHistImgRed, equalHistImgGreen, equalHistImgBlue))
plt.subplot(221), plt.imshow(imgRGB)
plt.subplot(222), plt.imshow(equalHistImgRGB)

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    srcHist = cv2.calcHist([img], [i], None, [256], [0, 256])
    tarHist = cv2.calcHist([equalHistImg], [i], None, [256], [0, 256])
    plt.subplot(223), plt.plot(srcHist, color=col)
    plt.subplot(224), plt.plot(tarHist, color=col)
    
plt.xlim([0, 256])
plt.show()
cv2.waitKey()
