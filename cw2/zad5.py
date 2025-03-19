import cv2 as cv

img = cv.imread('tiger.jpg')
(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)
tl = img[0:cY, 0:cX]
tr = img[0:cY,  cX:w]
bl = img[cY:h, 0:cX]
br = img[cY:h, cX:w]
img[0:cY, 0:cX] = (255, 0, 0)
cv.imshow('img', img)
cv.waitKey(0)
