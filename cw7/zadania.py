import cv2


# Zadanie 1: Odbicie poziome
def flip_horizontal(image):
    return cv2.flip(image, 1)


# Zadanie 2: Odbicie pionowe

def flip_vertical(image):
    return cv2.flip(image, 0)


# Zadanie 3: Odbicie względem obu osi
def flip_both(image):
    return cv2.flip(image, -1)


# Zadanie 4: Porównanie efektów (wyświetlenie 4 wersji obrazu)
def display_all_versions(image):
    hor = flip_horizontal(image)
    ver = flip_vertical(image)
    both = flip_both(image)

    cv2.imshow("Oryginal", image)
    cv2.imshow("Odbicie poziome", hor)
    cv2.imshow("Odbicie pionowe", ver)
    cv2.imshow("Odbicie obu osi", both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Zadanie 5: Zastosowanie odbicia na wybranym obszarze (środek obrazu)
def flip_selected_area(image):
    h, w = image.shape[:2]
    x1, y1 = w // 4, h // 4
    x2, y2 = 3 * w // 4, 3 * h // 4

    roi = image[y1:y2, x1:x2]
    flipped_roi = flip_horizontal(roi)
    image_copy = image.copy()
    image_copy[y1:y2, x1:x2] = flipped_roi

    cv2.imshow("Oryginal", image)
    cv2.imshow("Z wybranym obszarem odbitym", image_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Zadanie 6: Odbicie na podstawie wyboru użytkownika
def user_flip(image):
    print("Wybierz sposób odbicia: 0 – pionowe, 1 – poziome, -1 – oba")
    flip_code = int(input("Podaj kod odbicia: "))
    flipped = cv2.flip(image, flip_code)

    cv2.imshow("Oryginal", image)
    cv2.imshow("Odbity obraz", flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#####################################
# TESTING
#####################################

img = cv2.imread("image.jpg")
#img = flip_horizontal(img)
#img = flip_vertical(img)
#display_all_versions(img)
#flip_selected_area(img)
#user_flip(img)
#cv2.imshow("", img)
cv2.waitKey(0)
