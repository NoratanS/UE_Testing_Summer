import cv2
import numpy as np

# Wczytaj obraz binarny (upewnij się, że jest w tej samej lokalizacji lub podaj ścieżkę)
image = cv2.imread("shapes.jpg", cv2.IMREAD_GRAYSCALE)

# Konwertuj obraz na binarny, jeśli jeszcze nie jest
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Definicja różnych elementów strukturalnych
kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Erozja - kwadratowy kernel
eroded_square = cv2.erode(binary, kernel_square, iterations=3)

# Erozja - eliptyczny kernel
eroded_ellipse = cv2.erode(binary, kernel_ellipse, iterations=3)

# Wyświetl (jeśli chcesz)
cv2.imshow("Oryginalny", binary)
cv2.imshow("Erozja - kwadrat", eroded_square)
cv2.imshow("Erozja - elipsa", eroded_ellipse)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Figury się zmniejszają, w przypadku kwadratowego kernela stają się bardziej kanciaste
