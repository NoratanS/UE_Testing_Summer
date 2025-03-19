import cv2

img = cv2.imread("C:\\Users\\Krzysztof\\Pictures\\Profile-pic.png", cv2.IMREAD_GRAYSCALE)
if img.ndim == 2:
    print(1)
else:
    print(img.shape[2])
cv2.waitKey(0)
