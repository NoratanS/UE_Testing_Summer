import cv2
import numpy as np

# Wczytaj obraz z tablicą rejestracyjną
image = cv2.imread("plate_blurry.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 1. Wstępne przetwarzanie – podbicie kontrastu i binaryzacja
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
binary = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    11, 2
)

# 2. Zastosuj zamknięcie – połącz fragmenty liter
kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel_close)

# 3. Następnie otwarcie – usuń mały szum dookoła
kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
cleaned = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel_open)

# 4. Gradient – uwydatnienie konturów znaków
kernel_grad = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
gradient = cv2.morphologyEx(cleaned, cv2.MORPH_GRADIENT, kernel_grad)

cv2.imshow("Oryginalny", image)
cv2.imshow("Binaryzacja", binary)
cv2.imshow("Zamkniecie", closed)
cv2.imshow("Po otwarciu", cleaned)
cv2.imshow("Gradient", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
