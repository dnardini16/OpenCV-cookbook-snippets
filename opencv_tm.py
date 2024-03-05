import cv2
import os
import numpy as np

image = cv2.imread('image_tm.jpg')
template = cv2.imread('template.jpg')

w, h = template.shape[:-1]
res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.5
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

cv2.imwrite(os.path.join("outputs","tm.jpg"),image)