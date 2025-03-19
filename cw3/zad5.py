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
white = (255, 255, 255)

# loop over increasing radii, from 0 pixels to 150 pixels in 25
# pixel increments
for inc in range(0, 180, 10):
    # draw a white rectangle with the current 2inc size
    cv2.rectangle(canvas, (h // 2 - inc, w // 2 - inc), (h // 2 + inc, w // 2 + inc), white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
