import cv2
from cv2 import waitKey
import numpy as np

gambar = cv2.imread("Latihan/Gambar/2.jpg")
cv2.imshow("Gambar Asli", gambar)
baris, kolom = gambar.shape[:2]
geser = np.float32([[1, 0, 100], [0, 1, 50]])
gambar2 = cv2.warpAffine(gambar, geser, (kolom, baris))
cv2.imshow("gambar di rotasi", gambar2)
waitKey(0)
