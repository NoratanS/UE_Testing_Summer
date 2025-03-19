import cv2

img = cv2.imread("C:\\Users\\Krzysztof\\Pictures\\Profile-pic.png", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("C:\\Users\\Krzysztof\\Desktop\\dragon.png", img)

cv2.waitKey(0)
