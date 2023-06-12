import cv2
from cv2 import waitKey

gambar = cv2.imread("Latihan/Gambar/3.jpg")
cv2.imshow("Gambar Asli", gambar)
baris, kolom = gambar.shape[:2]
putar = cv2.getRotationMatrix2D((kolom / 2, baris / 2), 90, 1)
gambar2 = cv2.warpAffine(gambar, putar, (kolom, baris))
cv2.imshow("gambar di rotasi", gambar2)
waitKey(0)
