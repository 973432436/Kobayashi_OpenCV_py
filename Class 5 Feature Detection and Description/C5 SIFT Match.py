import cv2
import numpy as np

img1 = cv2.imread('Mavic Air Fly.jpeg')
img2 = cv2.imread('Mavic Air Fly yuntai.jpeg')
matchImg = np.zeros_like(img1)

grayImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayImg2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(grayImg1, None)
kp2, des2 = sift.detectAndCompute(grayImg2, None)

bf = cv2.BFMatcher_create(normType=cv2.NORM_L2, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
matchImg = cv2.drawMatches(img1, kp1, img2, kp2, matches, matchImg, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
# bf = cv2.BFMatcher_create(normType=cv2.NORM_L2, crossCheck=False)
# matches = bf.knnMatch(des1, des2, k=2)
# 使用阈值筛选距离
# good = []
# for m, n in matches:
#  if m.distance < 0.05*n.distance:
#     good.append([m])
#
# matchImg = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, matchImg, flags=2)

cv2.imshow('Match Image', matchImg)

cv2.waitKey()
cv2.destroyAllWindows()
