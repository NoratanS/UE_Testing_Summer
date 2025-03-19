import cv2
import numpy as np

image = cv2.imread("example.jpg")
cv2.imshow("original", image)
cv2.waitKey(0)

M3 = np.float32([[1, 0, image.shape[1]//2 + 50], [0, 1, image.shape[0]//2 + 50]])
shifted3 = cv2.warpAffine(image, M3, (image.shape[1], image.shape[0]))
cv2.imshow("big shift", shifted3)
cv2.waitKey(0)
