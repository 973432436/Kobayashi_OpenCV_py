import cv2
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    pass


img = cv2.imread('hand1.jpg')
ROI = cv2.imread('hand1ROI.jpg')

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
roiHSV = cv2.cvtColor(ROI, cv2.COLOR_BGR2HSV)
cv2.namedWindow('BackProjection Image')
cv2.createTrackbar('H Value', 'BackProjection Image', 0, 180, nothing)

while(1):

    hSize = cv2.getTrackbarPos('H Value', 'BackProjection Image')
    hSize = max(2, hSize)
    roiHSVHist = cv2.calcHist([roiHSV], [0, 1], None, [hSize, 256], [0, 180, 0, 256])
    cv2.normalize(roiHSVHist, roiHSVHist, 0, 255, cv2.NORM_MINMAX)
    backProjImg = cv2.calcBackProject([imgHSV], [0, 1], roiHSVHist, [0, 180, 0, 256], 1)
    cv2.imshow('BackProjection Image', backProjImg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

cv2.waitKey()

