# import the necessary packages
import numpy as np
import cv2
# initialize our canvas as a 300x300 pixel image with 3 channels
# (Red, Green, and Blue) with a black background
img = cv2.imread('janpawel2.jpg')
(x, y, c) = img.shape
print(x, y, c)

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

cv2.circle(img, (120, 130), 30, red, -1)
cv2.circle(img, (180, 130), 30, red, -1)
cv2.rectangle(img, (100, 180), (180, 210), green, -1)
cv2.circle(img, (130, 130), 130, blue, 1)

cv2.imshow('img', img)
cv2.waitKey(0)
