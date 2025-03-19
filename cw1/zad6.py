import cv2

img_color = cv2.imread("C:\\Users\\Krzysztof\\Pictures\\Profile-pic.png")
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", img_color)
cv2.waitKey(0)

