import cv2 as cv

img = cv.imread('tiger.jpg')
(h,w) = img.shape[:2]
img[100] = [(0,255,0)] * w
cv.imshow('tiger.jpg', img)
cv.waitKey(0)