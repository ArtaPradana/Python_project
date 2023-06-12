import cv2
import numpy as np

img = cv2.imread("Latihan/Gambar/3.jpg", 0)
cv2.imshow("Original image", img)

row, column = img.shape

img1 = np.zeros((row, column), dtype="uint8")

min_range = 70
max_range = 135

for i in range(row):
    for j in range(column):
        if img[i, j] > min_range and img[i, j] < max_range:
            img1[i, j] = 255
        else:
            img1[i, j] = 0

cv2.imshow("sliced image", img1)
cv2.waitKey(0)
