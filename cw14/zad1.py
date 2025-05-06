import cv2

image = cv2.imread("golden.jpg")
cv2.imshow("Oryginalny obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Parametry do testów
kernel_sizes = [(3, 3), (5, 5), (9, 9), (15, 15)]

# Proste rozmycie (Average blur)
for (kX, kY) in kernel_sizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow(f"Średnie rozmycie ({kX}x{kY})", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Rozmycie Gaussa
for (kX, kY) in kernel_sizes:
    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow(f"Rozmycie Gaussa ({kX}x{kY})", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Rozmycie medianowe
for k in [3, 9, 15]:
    blurred = cv2.medianBlur(image, k)
    cv2.imshow(f"Rozmycie medianowe ({k}x{k})", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Rozmycie dwustronne
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
for (d, sc, ss) in params:
    blurred = cv2.bilateralFilter(image, d, sc, ss)
    cv2.imshow(f"Bilateral d={d}, sc={sc}, ss={ss}", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Komentarze:
# - Rozmycie medianowe najlepiej usuwa szum typu "sól i pieprz"
# - Rozmycie dwustronne zachowuje najwięcej szczegółów i krawędzi
# - Rozmycie średnie i gaussowskie są szybsze, ale tracą więcej detali
