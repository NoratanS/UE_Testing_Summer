import cv2

img_gray = cv2.imread("C:\\Users\\Krzysztof\\Pictures\\Profile-pic.png", cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("C:\\Users\\Krzysztof\\Pictures\\Profile-pic.png")
cv2.imshow("Original", img_color)
cv2.imshow("Grayscale", img_gray)

w = 2
while w != 0:
    k = cv2.waitKey(0)
    if k == ord('o'):
        cv2.destroyWindow("Original")
        w -= 1
    elif k == ord('g'):
        cv2.destroyWindow("Grayscale")
        w -= 1
