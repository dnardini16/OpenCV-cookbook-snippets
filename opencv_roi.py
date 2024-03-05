import cv2
import os

image = cv2.imread("image.jpg")
x,y,w,h = 0,0,3000,1500
roi = image[y:y+h, x:x+w]
cv2.imwrite(os.path.join("outputs","roi.jpg"),roi)