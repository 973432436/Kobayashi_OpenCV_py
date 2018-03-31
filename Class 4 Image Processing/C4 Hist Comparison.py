import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('noodle1.JPG')
img2 = cv2.imread('noodle2.JPG')
img3 = cv2.imread('noodle3.JPG')

grayImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayImg2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
grayImg3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
img1RGB = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2RGB = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img3RGB = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)

grayHist1 = cv2.calcHist([grayImg1], [0], None, [256], [0, 256])
grayHist2 = cv2.calcHist([grayImg2], [0], None, [256], [0, 256])
grayHist3 = cv2.calcHist([grayImg3], [0], None, [256], [0, 256])

result1 = cv2.compareHist(grayHist1, grayHist2, cv2.HISTCMP_CORREL)
result2 = cv2.compareHist(grayHist1, grayHist3, cv2.HISTCMP_CORREL)
print(result1)
print(result2)

plt.subplot(231), plt.imshow(img1RGB)
plt.subplot(232), plt.imshow(img2RGB)
plt.subplot(233), plt.imshow(img3RGB)
plt.subplot(234), plt.plot(grayHist1)
plt.subplot(235), plt.plot(grayHist2)
plt.subplot(236), plt.plot(grayHist3)
plt.show()

cv2.waitKey()
