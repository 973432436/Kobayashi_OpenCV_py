import cv2
import numpy as np

img1 = cv2.imread('E:\\OpenCV\\py_version\\demo\\venv\\Picture\\Mavic Air Fly.jpeg')
img2 = cv2.imread('E:\\OpenCV\\py_version\\demo\\venv\\Picture\\Mavic Air Fly yuntai Erected.jpeg')
grayImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayImg2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
matchImg = np.zeros_like(img1)

surf = cv2.xfeatures2d.SURF_create(2000)
kp1, des1 = surf.detectAndCompute(grayImg1, None)
kp2, des2 = surf.detectAndCompute(grayImg2, None)

bf = cv2.BFMatcher_create(crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
matchImg = cv2.drawMatches(img1, kp1, img2, kp2, matches, matchImg, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv2.imshow('SURF Image', matchImg)
cv2.imwrite('surfMatch.jpg', matchImg)
cv2.waitKey()
cv2.destroyAllWindows()
