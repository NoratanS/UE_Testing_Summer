import cv2

# Wczytaj obraz
image = cv2.imread("plate_blurry.jpg", cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Typy kerneli
kernel_shapes = {
    "kwadrat": cv2.MORPH_RECT,
    "krzyz": cv2.MORPH_CROSS,
    "elipsa": cv2.MORPH_ELLIPSE
}

# Rozmiar kernela (stały, żeby lepiej porównać)
kernel_size = (2, 2)

# Operacje morfologiczne do wykonania
operations = {
    "erozja": cv2.MORPH_ERODE,
    "dylatacja": cv2.MORPH_DILATE,
    "otwarcie": cv2.MORPH_OPEN,
    "zamkniecie": cv2.MORPH_CLOSE,
    "gradient": cv2.MORPH_GRADIENT
}

# Wykonaj operacje dla każdego typu kernela
for shape_name, shape_type in kernel_shapes.items():
    kernel = cv2.getStructuringElement(shape_type, kernel_size)
    for op_name, op_code in operations.items():
        result = cv2.morphologyEx(binary, op_code, kernel)
        cv2.imshow(f"{op_name} ({shape_name})", result)

cv2.imshow("original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
