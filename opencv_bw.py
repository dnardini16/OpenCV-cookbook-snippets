import cv2
import os

image = cv2.imread("image.jpg")
bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(os.path.join("outputs","bw.jpg"),bw)