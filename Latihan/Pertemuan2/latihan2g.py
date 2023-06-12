# memanggil library opencv
import cv2
from cv2 import waitKey

# menyimpan gambar dengan fungsi imread dari OpenCV
img = cv2.imread("Latihan/Gambar/2.jpg")
# sesuaikan dengan nama file yang diunggah pada cell sebelumnya
# menampilkan gambar dengan fungsi cv2_imshow
cv2.imshow("Lena", img)
waitKey(0)
# lihat tipe data img. disimpan sebagai apa?
print(type(img))
print(img.shape)  # menampilkan resolusi
print(img.size)  # menampilkan ukuran data pada media penyimpan
print(img.dtype)  # image datatype (kedalaman bit)

# Band blue, green dan red masng-masing disimpan pada variabel b,g,r
b, g, r = cv2.split(img)
b = img[..., 0]  # blue channel
g = img[..., 1]  # green channel
r = img[..., 2]  # red channel
