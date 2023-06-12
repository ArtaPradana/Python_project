import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("Latihan/Gambar/3.jpg")
H, W = img.shape[:2]
gray = np.zeros((H, W), np.uint8)
for i in range(H):
    for j in range(W):
        # Perhatikan format gambar B,G,R
        gray[i, j] = np.clip(
            0.299 * img[i, j, 2] + 0.587 * img[i, j, 1] + 0.114 * img[i, j, 0], 0, 255
        )
fig = plt.figure()
fig.add_subplot(211)
plt.imshow(img)
fig.add_subplot(212)
plt.imshow(gray)
plt.show()
