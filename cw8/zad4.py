import cv2
import numpy as np

# Wczytanie obrazu
image = cv2.imread('img.jpg')

# 4. Dynamiczny wybór ROI
startX = int(input("Podaj startX: "))
endX = int(input("Podaj endX: "))
startY = int(input("Podaj startY: "))
endY = int(input("Podaj endY: "))
dynamic_roi = image[startY:endY, startX:endX]
cv2.imshow("Dynamiczny ROI", dynamic_roi)
cv2.waitKey(0)
