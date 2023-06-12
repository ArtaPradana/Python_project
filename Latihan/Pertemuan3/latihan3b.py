import cv2
from cv2 import waitKey
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("gambar/lena.jpg")
cv2.imshow("Gambar Asli", img)
waitKey(0)
# mengubah ke greyscale menggunakan function pada OpenCV
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
brightness = 50
h, w = img2.shape[:2]
# perulangan untuk melakukan proses pertambahan
for i in np.arange(h):
    for j in np.arange(w):
        a = img2.item(i, j)
b = a + brightness
if b > 255:
    b = 255
elif b < 0:
    b = 0
else:
    b = b
img2.itemset((i, j), b)
img1 = cv2.imread("Latihan/Gambar/2.jpg")
img2 = cv2.imread("Latihan/Gambar/3.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
op_and = cv2.bitwise_and(img1, img2)
op_or = cv2.bitwise_or(img1, img2)
op_xor = cv2.bitwise_xor(img1, img2)
cv2.imshow("Image 1", img1)
waitKey(0)
cv2.imshow("Image 2", img2)
waitKey(0)
cv2.imshow("And", op_and)
waitKey(0)
cv2.imshow("OR", op_or)
waitKey(0)
cv2.imshow("XOR", op_xor)
waitKey(0)
