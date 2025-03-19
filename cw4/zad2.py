import cv2
import numpy as np

image = cv2.imread("example.jpg")
cv2.imshow("original", image)
cv2.waitKey(0)

M2 = np.float32([[1, 0, -20], [0, 1, -50]])
shifted2 = cv2.warpAffine(image, M2, (image.shape[1], image.shape[0]))
cv2.imshow("20px left, 50px up", shifted2)
cv2.waitKey(0)
