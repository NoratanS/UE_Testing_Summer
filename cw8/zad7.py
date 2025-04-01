import cv2
import numpy as np

# Wczytanie obrazu
image = cv2.imread('img.jpg')

# 7. ZNOWU PUZZLE!!!
h, w = image.shape[:2]
ph, pw = h // 3, w // 3
for row in range(3):
    for col in range(3):
        tile = image[row*ph:(row+1)*ph, col*pw:(col+1)*pw]
        cv2.imshow(f"Tile {row},{col}", tile)
cv2.waitKey(0)
