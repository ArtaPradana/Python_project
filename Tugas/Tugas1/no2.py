import cv2
from cv2 import waitKey

G1 = cv2.imread("Tugas/gambar/luffy2.jpeg", 0)

G2 = cv2.imread("Tugas/gambar/itachi.jpg", 0)

citra_add = cv2.add(G1, G2)

citra_sub = cv2.subtract(G1, G2)

cv2.imwrite("Tugas/gambar/hasil_penjumlahan.jpg", citra_add)
cv2.imwrite("Tugas/gambar/hasil_pengurangan.jpg", citra_sub)

cv2.imshow("Gambar Penambahan", citra_add)
cv2.imshow("Gambar Pengurangan", citra_sub)
cv2.waitKey(0)
