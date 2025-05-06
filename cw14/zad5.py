import cv2
import numpy as np


# Dodanie szumu typu "sól i pieprz"
def salt_and_pepper(image, amount=0.05):
    noisy = image.copy()
    num_salt = np.ceil(amount * image.size * 0.5).astype(int)
    coords = [np.random.randint(0, i, num_salt) for i in image.shape[:2]]
    noisy[coords[0], coords[1]] = 255

    num_pepper = np.ceil(amount * image.size * 0.5).astype(int)
    coords = [np.random.randint(0, i, num_pepper) for i in image.shape[:2]]
    noisy[coords[0], coords[1]] = 0
    return noisy


image = cv2.imread('golden.jpg')
cv2.imshow('Oryginal', image)
noisy_image = salt_and_pepper(image, 0.03)
cv2.imshow("Zaszumiony", noisy_image)

# Porównanie metod
cv2.imshow("Median", cv2.medianBlur(noisy_image, 5))
cv2.imshow("Gaussian", cv2.GaussianBlur(noisy_image, (5, 5), 0))
cv2.imshow("Bilateral", cv2.bilateralFilter(noisy_image, 9, 75, 75))

# Komentarze:
# - Rozmycie medianowe najskuteczniejsze w usuwaniu "soli i pieprzu"
# - Gaussian i Bilateral lepsze dla szumu Gaussa

cv2.waitKey(0)
cv2.destroyAllWindows()
