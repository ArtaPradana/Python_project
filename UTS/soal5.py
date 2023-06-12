import cv2
from matplotlib import pyplot as plt

G1 = cv2.imread("UTS/gambar/red.jpg", 0)
G2 = cv2.imread("UTS/gambar/mikey.jpg", 0)

subtracted_image = cv2.subtract(G2, G1)
equalized_image = cv2.equalizeHist(subtracted_image)

plt.subplot(2, 2, 1)
plt.imshow(G1, cmap="gray")
plt.title("G1")
plt.subplot(2, 2, 2)
plt.imshow(G2, cmap="gray")
plt.title("G2")
plt.subplot(2, 2, 3)
plt.imshow(subtracted_image, cmap="gray")
plt.title("G2-G2")
plt.subplot(2, 2, 4)
plt.hist(equalized_image.ravel(), 256, [0, 256])
plt.title("Histogram G2 - G1 (Setelah Di Ekualisasi)")
plt.show()
