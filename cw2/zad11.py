import cv2 as cv
import numpy as np

img = cv.imread('tiger.jpg')
(h, w) = img.shape[:2]
max = 0
max_i = 0
max_j = 0
for i in range(0, h):
    for j in range(0, w):
        if np.mean(img[i, j]) > max:
            max = np.mean(img[i, j])
            max_i = i
            max_j = j

print(max, (max_i, max_j))