import cv2
import numpy as np
from cv2 import waitKey
#input image
img = cv2.imread('Latihan/Gambar/5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY_INV
+cv2.THRESH_OTSU)
cv2.imshow('image', thresh)
# Construct the structuring element
kernel = np.array((
[1, 1, 1],
[0, 1, -1],
[0, 1, -1]), dtype="int")
# Apply hit-or-miss transformation
output_image = cv2.morphologyEx(thresh, cv2.MORPH_HITMISS, kernel)
cv2.imshow('image asal', img)
cv2.imshow('image hasil', output_image)
waitKey(0)