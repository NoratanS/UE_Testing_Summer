import cv2 as cv

img = cv.imread('tiger.jpg')
(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)
img[cY-50:cY+50, cX-50:cX+50] = (0,0,255)
cv.imshow('img', img)
cv.waitKey(0)
