import cv2
import os

image = cv2.imread("image.jpg")
resized_image = cv2.resize(image, (200, 200))
cv2.imwrite(os.path.join("outputs","resized_image.jpg"),resized_image)