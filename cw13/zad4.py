import cv2
import numpy as np

# Wczytaj obraz z przerwami w konturach znaków (np. zeskanowany tekst)
image = cv2.imread("smile.jpg", cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)  # Zamieniamy: tło czarne, litery białe

# Różne elementy strukturalne
kernels = {
    "rect": cv2.getStructuringElement(cv2.MORPH_RECT, (30, 30)),
    "ellise": cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (30, 30))
}

# Zastosuj zamknięcie
for name, kernel in kernels.items():
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    cv2.imshow(f"closing-{name}", closing)

# Pokaż oryginał
cv2.imshow("original", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
