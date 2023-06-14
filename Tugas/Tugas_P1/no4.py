import cv2

img = cv2.imread("Tugas/gambar/hasil_penjumlahan.jpg", 1)

img_ref_v = cv2.flip(img, 0)

cv2.imshow("Gambar Asli", img)
cv2.imshow("Refleksi Vertikal", img_ref_v)
cv2.waitKey(0)
