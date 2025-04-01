import cv2
import numpy as np

# Wczytanie obrazu
image = cv2.imread('img.jpg')
h, w = image.shape[:2]

# 8. Animacja ROI
x = 0
while x + 200 <= w:
    roi = image[:, x:x+200]
    cv2.imshow("Przesuwajacy ROI", roi)
    key = cv2.waitKey(0)  # czeka na klawisz
    if key == ord('q'):
        break
    x += 10

