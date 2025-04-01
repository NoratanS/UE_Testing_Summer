import cv2
import numpy as np

# Wczytanie obrazu
image = cv2.imread('img.jpg')

# 6. Kopiowanie i wklejanie fragmentu obrazu
fragment = image[0:100, 0:100]
copy_image = image.copy()
copy_image[100:200, 100:200] = fragment
cv2.imshow("Z wklejonym fragmentem", copy_image)
cv2.waitKey(0)
