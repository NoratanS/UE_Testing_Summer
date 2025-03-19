import cv2 as cv

img = cv.imread('tiger.jpg')
(b1, g1, r1) = img[50][50]
(b2, g2, r2) = img[200][200]
print(abs(b1 - b2), abs(g1 - g2), abs(r1 - r2))
