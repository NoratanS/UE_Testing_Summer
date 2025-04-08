import cv2
import numpy as np

img = cv2.imread('person.jpg')
cv2.imshow('person', img)

mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.circle(mask, (390, 170), 25, 255, -1)
cv2.circle(mask, (460, 170), 25, 255, -1)
cv2.imshow("Rectangular Mask", mask)


masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
