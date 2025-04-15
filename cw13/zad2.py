import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Wczytaj obraz w skali szarości
image = cv2.imread("lines.jpg", cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Element strukturalny - prostokątny 3x3
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Lista wyników do analizy grubości
dilated_images = []
iterations_range = [1, 2, 3, 4, 5]

for i in iterations_range:
    dilated = cv2.dilate(binary, kernel, iterations=i)
    dilated_images.append((i, dilated))
    cv2.imshow(f"dilated {i}", dilated)
# Opcjonalnie: wykres grubości (dla uproszczenia: liczba pikseli != 0)
thicknesses = [np.count_nonzero(img) for _, img in dilated_images]

plt.plot(iterations_range, thicknesses, marker='o')
plt.title("Wpływ iteracji dylatacji na grubość obiektów")
plt.xlabel("Liczba iteracji")
plt.ylabel("Liczba pikseli pierwszoplanowych")
plt.grid(True)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()