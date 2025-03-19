import cv2
import numpy as np

image = cv2.imread("example.jpg")
cv2.imshow("original", image)
cv2.waitKey(0)

tx = int(input("horizontal shift: "))
print("\n")
ty = int(input("vertical shift: "))
M5 = np.float32([[1, 0, tx], [0, 1, ty]])
shifted5 = cv2.warpAffine(image, M5, (image.shape[1], image.shape[0]))
cv2.imshow(f"dynamic shift {tx}px, {ty}px", shifted5)
cv2.waitKey(0)

cv2.destroyAllWindows()
