import cv2
import numpy as np

image = cv2.imread("Latihan/Pertemuan14/train/banana_40.jpg")
cv2.imshow("Gambar Asli", image)
# cv2.waitKey()

width = 150
height = 150
dim = (width, height)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Gambar Resized", resized)
cv2.waitKey()

hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

# color_featur = []
h_mean = np.mean(h)
s_mean = np.mean(s)
v_mean = np.mean(v)

h_std = np.std(h)
s_std = np.std(s)
v_std = np.std(v)

fitur = [h_mean, s_mean, v_mean, h_std, s_std, v_std]
print(fitur)
cv2.waitKey()
