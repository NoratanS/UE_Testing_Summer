import cv2
import numpy as np

# Wczytanie obrazu
image = cv2.imread('img.jpg')

# 3. Prawa połowa obrazu
h, w = image.shape[:2]
prawa_polowa = image[:, w//2:]
cv2.imshow("Dolna polowa", prawa_polowa)
cv2.waitKey(0)
