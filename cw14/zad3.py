import cv2

image = cv2.imread("noisy_edges.jpg")

# Zastosuj rozmycie dwustronne
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
for (d, sc, ss) in params:
    blurred = cv2.bilateralFilter(image, d, sc, ss)
    cv2.imshow(f"Bilateral d={d}, sc={sc}, ss={ss}", blurred)

# Komentarze:
# - Rozmycie dwustronne redukuje szum skutecznie
# - Zachowuje lepiej krawędzie niż inne metody
# - Najlepsze efekty przy d=11, sigmaColor=41, sigmaSpace=21

cv2.waitKey(0)
cv2.destroyAllWindows()
