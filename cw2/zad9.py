import cv2 as cv

img = cv.imread('tiger.jpg')
img[50:100, 50:100] = (255,255,255)
cv.imshow('tiger.jpg', img)
cv.waitKey(0)