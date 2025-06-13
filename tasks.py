import argparse
import imutils
import cv2

# load the image and show it
image = cv2.imread("image.png")
image = cv2.resize(image, (640, 480), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Original", image)

# grab the dimensions of the image and calculate the center of the
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)


# image
def rotate_and_show_image(image=image, center=(0, 0), angle=45, scale=1.0):
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow(f"Rotated by {angle} Degrees", rotated)
    return rotated


def rotate_and_show_imutils(image=image, center=(0, 0), angle=45, scale=1.0, rotate_bound=False):
    if rotate_bound:
        rotated = imutils.rotate_bound(image, angle)
        cv2.imshow(f"Rotated by {angle} without cropping (imutils)", rotated)
    else:
        rotated = imutils.rotate(image=image, center=center, angle=angle, scale=scale)
        cv2.imshow(f"Rotated by {angle} (imutils)", rotated)
    return rotated


# Task 1
rotate_and_show_image(image=image, center=(cX, cY), angle=45, scale=1.0)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Task 2
rotate_and_show_image(image=image, center=(cX, cY), angle=-90, scale=1.0)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Task 3
rotate_and_show_image(image=image, angle=30, scale=1.0)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Task 4
# Just pass the angle argument...
rotate_and_show_image(image=image, center=(cX, cY), angle=69, scale=1.0)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Task 5
rotate_and_show_imutils(image=image, center=(cX, cY), angle=180, scale=1.0)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Task 6
rotate_and_show_imutils(image=image, center=(cX, cY), angle=-33, scale=1.0, rotate_bound=True)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Task 7
rotate_and_show_image(image=image, center=(cX, cY), angle=60, scale=1.0)
rotate_and_show_imutils(image=image, center=(cX, cY), angle=60, scale=1.0)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Task 8
seq_rotated = image.copy()
for i in range(3):
    seq_rotated = rotate_and_show_image(image=seq_rotated, center=(cX, cY), angle=30)
rotate_and_show_image(image=image, center=(cX, cY), angle=90)

cv2.waitKey()
cv2.destroyAllWindows()

# Task 9
img_to_save = image.copy()
img_to_save = rotate_and_show_image(image=img_to_save, center=(cX, cY), angle=75, scale=1.0)
cv2.imwrite("rotated_output.jpg", img_to_save)
cv2.waitKey()
cv2.destroyAllWindows()

# Task 10
seq_rotated = image.copy()
for i in range(15, 361, 15):
    seq_rotated = rotate_and_show_image(image=seq_rotated, center=(cX, cY), angle=i)
    cv2.waitKey(500)
    cv2.destroyAllWindows()

