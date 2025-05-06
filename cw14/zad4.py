import cv2

image = cv2.imread("road_sign.jpg")

for method in ["blur", "gaussian", "median", "bilateral"]:
    if method == "blur":
        blurred = cv2.blur(image, (9, 9))
    elif method == "gaussian":
        blurred = cv2.GaussianBlur(image, (9, 9), 0)
    elif method == "median":
        blurred = cv2.medianBlur(image, 9)
    else:
        blurred = cv2.bilateralFilter(image, 9, 75, 75)

    cv2.imshow(f"{method}", blurred)

# Komentarze:
# - Metoda blur i gaussian najmocniej rozmywają tekst
# - Bilateral i median pozwalają lepiej zachować jego czytelność

cv2.waitKey(0)
cv2.destroyAllWindows()
