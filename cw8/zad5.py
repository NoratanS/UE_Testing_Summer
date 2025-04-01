import cv2
import numpy as np

# Wczytanie obrazu

image = cv2.imread('img.jpg')
startX = 125
endX = 325
startY = 75
endY = 225
dynamic_roi = image[startY:endY, startX:endX]
cv2.imshow("Panda face", dynamic_roi)
cv2.waitKey(0)
