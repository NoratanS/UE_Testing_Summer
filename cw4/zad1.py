import cv2
import numpy as np

# Wczytanie obrazu
image = cv2.imread("example.jpg")
cv2.imshow("original", image)
cv2.waitKey(0)

M1 = np.float32([[1, 0, 30], [0, 1, 40]])
shifted1 = cv2.warpAffine(image, M1, (image.shape[1], image.shape[0]))
cv2.imshow("30px right, 40px down", shifted1)
cv2.waitKey(0)
