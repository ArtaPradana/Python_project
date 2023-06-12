import cv2

gambar = cv2.imread("Latihan/Gambar/2.jpg")
# window_name = 'Gambar Refleksi'
gambar2 = cv2.flip(gambar, 0)
# Displaying the image
cv2.imshow("asli", gambar)
cv2.imshow("Gambar refleksi", gambar2)
cv2.waitKey(0)
