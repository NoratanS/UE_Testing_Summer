import cv2
import numpy as np

img = cv2.imread('car.jpg')
cv2.imshow('original', img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)

# c. Zakres koloru do ekstrakcji — np. czerwony
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

# Czerwony ma dwa zakresy w HSV, więc dodajemy drugi
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

# Połącz maski
mask = cv2.bitwise_or(mask1, mask2)

# d. Użycie maski do wyciągnięcia tylko wybranego koloru z oryginalnego obrazu
result = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('car', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
