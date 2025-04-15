import cv2
import numpy as np

# Wczytaj obraz z szumem
image = cv2.imread("balloons_noisy.png", cv2.IMREAD_GRAYSCALE)

# Progowanie (upewnij się, że mamy obraz binarny)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Różne rozmiary kerneli
kernel_sizes = [(2, 2), (3, 3)]

# Wykonaj operację otwarcia i zapisz wyniki
for size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    # Pokaż efekt
    cv2.imshow(f"kernel-{size}", opening)

# Oryginalny dla porównania
cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
