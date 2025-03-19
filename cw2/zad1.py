import cv2 as cv

img = cv.imread('tiger.jpg')
first_px = img[0, 0]
print(first_px[::-1])
