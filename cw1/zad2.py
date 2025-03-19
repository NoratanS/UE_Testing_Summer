import cv2

img = cv2.imread("C:\\Users\\Krzysztof\\Pictures\\Profile-pic.png")
print(img.shape[2])
cv2.waitKey(0)
