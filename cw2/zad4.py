import cv2 as cv


def get_user_input():
    x = input("podaj x\n")
    y = input("podaj y\n")
    return int(x), int(y)


img = cv.imread('tiger.jpg')
(h, w) = img.shape[:2]
print(h, w)

(x, y) = get_user_input()
while x < 0 or y < 0 or x >= h or y >= w:
    print("poza zakresem")
    (x, y) = get_user_input()

img[x, y] = (0, 0, 255)
cv.imshow('img', img)
cv.waitKey(0)

