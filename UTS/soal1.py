import cv2
from matplotlib import pyplot as plt

image = cv2.imread("UTS/gambar/luffy.jpg", 0)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.plot(hist)
plt.title("Histogram G1")
plt.show()
