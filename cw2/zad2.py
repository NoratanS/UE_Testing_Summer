import cv2 as cv

img = cv.imread('tiger.jpg')
cv.imshow('before', img)
(h, w) = img.shape[:2]
img[h - 1, w - 1] = (0, 0, 255)
cv.imshow('after', img)
cv.waitKey(0)
