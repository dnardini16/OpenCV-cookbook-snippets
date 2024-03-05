import cv2
import os

image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

## 180 degrees rotation
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated_image = cv2.warpAffine(image, M, (w, h))

cv2.imwrite(os.path.join("outputs","rotated_image.jpg"),rotated_image)