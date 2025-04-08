# import the necessary packages
import numpy as np
import cv2
# draw a rectangle
# Create a blank black image
triangle = np.zeros((300, 300), dtype="uint8")

# Define triangle points
pts = np.array([[275, 25], [25, 25], [275, 275]], dtype=np.int32)

# Reshape for drawContours: needs (n_points, 1, 2)
pts = pts.reshape((-1, 1, 2))
cv2.drawContours(triangle, [pts], contourIdx=0, color=255, thickness=-1)
cv2.imshow("Triangle", triangle)

# draw a circle
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

bitwiseOr = cv2.bitwise_or(triangle, circle)
bitwiseAnd = cv2.bitwise_and(triangle, circle)
bitwiseXor = cv2.bitwise_xor(triangle, circle)
bitwiseTriNot = cv2.bitwise_not(triangle)
bitwiseCirNot = cv2.bitwise_not(circle)

cv2.imshow("Bitwise OR", bitwiseOr)
cv2.imshow("Bitwise AND", bitwiseAnd)
cv2.imshow("Bitwise XOR", bitwiseXor)
cv2.imshow("Bitwise NOT TRIANGLE", bitwiseTriNot)
cv2.imshow("Bitwise NOT CIRCLE", bitwiseCirNot)

cv2.waitKey(0)
cv2.destroyAllWindows()