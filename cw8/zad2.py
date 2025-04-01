import cv2
import numpy as np

# Wczytanie obrazu
image = cv2.imread('img.jpg')

# 2. Dolna połowa obrazu
h, w = image.shape[:2]
dolna_polowa = image[h//2:, :]
cv2.imshow("Dolna polowa", dolna_polowa)
cv2.waitKey(0)
