# import the necessary packages
import numpy as np
import cv2
# initialize our canvas as a 300x300 pixel image with 3 channels
# (Red, Green, and Blue) with a black background
canvas = np.zeros((300, 300, 3), dtype="uint8")

(h, w, c) = canvas.shape
print(h, w, c)

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

cv2.rectangle(canvas, (0, 0), (100, 50), green, 2)
cv2.rectangle(canvas, (h, w), (h - 100, w - 50), red, 3)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
