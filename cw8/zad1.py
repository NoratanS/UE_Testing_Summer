import cv2
import numpy as np

# Wczytanie obrazu
image = cv2.imread('img.jpg')

# 1. ROI: lewy górny róg 100x100
roi_1 = image[0:100, 0:100]
cv2.imshow("ROI 100x100", roi_1)
cv2.waitKey(0)