import cv2
import numpy as np


image = cv2.imread("flowers.jpg")
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (100, 400), (500, 700), 255, -1)  # Przykład maski

blurred = cv2.GaussianBlur(image, (31, 31), 0)
focus = np.where(mask[:, :, None] == 255, image, blurred)

cv2.imshow("Efekt głębi ostrości", focus)

# Komentarz:
# - Technika skutecznie imituje efekt głębi ostrości
# - Można ją rozszerzyć o segmentację tła lub detekcję obiektów

cv2.waitKey(0)
cv2.destroyAllWindows()
