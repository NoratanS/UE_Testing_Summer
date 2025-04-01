import cv2
import numpy as np

# Wczytanie obrazu
image = cv2.imread('img.jpg')

# 9. Zapis przyciętego obrazu
cropped = image[0:300, 0:300]
cv2.imwrite("cropped_image.jpg", cropped)
cv2.imshow("Zapisany obszar", cropped)
cv2.waitKey(0)
