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

cv2.circle(canvas, (40, 40), 40, blue, -1)
cv2.circle(canvas, (h // 2, w // 2), 60, red, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
