import cv2
import os

image = cv2.imread("image.jpg")
blurred_image = cv2.blur(image, (50, 50))
cv2.imwrite(os.path.join("outputs","blurred_image.jpg"),blurred_image)