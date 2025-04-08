# import the necessary packages
import numpy as np
import cv2
# draw a rectangle
rectangle1 = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle1, (25, 25), (275, 275), 255, -1)

rectangle2 = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle2, (24, 24), (276, 276), 255, -1)

bitwise_XOR = np.bitwise_xor(rectangle1, rectangle2)
cv2.imshow("rectangle1", rectangle1)
cv2.imshow("rectangle2", rectangle2)
cv2.imshow("XOR", bitwise_XOR)
cv2.waitKey(0)
