import cv2
from cv2 import waitKey

img = cv2.imread("Latihan/Gambar/3.jpg")
# konversi BGR dari variable img ke colorspace HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# memisahkan hue, saturation dan value
h, s, v = cv2.split(hsv)
# menampilkan band hue
cv2.imshow("Hasil", h)
waitKey(0)
cv2.imshow("Hasil", img)
waitKey(0)
