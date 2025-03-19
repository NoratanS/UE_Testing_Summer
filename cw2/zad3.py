import cv2 as cv

img = cv.imread('tiger.jpg')
(h, w) = img.shape[:2]
print(h, w)
(cX, cY) = (w // 2, h // 2)
print(cX, cY)
print(img[cX, cY])
