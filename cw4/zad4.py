import cv2
import imutils

image = cv2.imread("example.jpg")
cv2.imshow("original", image)
cv2.waitKey(0)

shifted4 = imutils.translate(image, 100, 50)
cv2.imshow("100px right, 50px down (imutils)", shifted4)
cv2.waitKey(0)
