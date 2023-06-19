import cv2
import numpy as np
from scipy.stats import skew


def extract_color_moments(image):
    # Mengubah citra menjadi ruang warna LAB
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Menghitung histogram warna LAB
    hist = cv2.calcHist([lab_image], [1, 2], None, [8, 8], [0, 256, 0, 256])

    # Normalisasi histogram
    hist /= hist.sum()

    # Menghitung momen warna
    mean = np.mean(hist)
    std_dev = np.std(hist)
    skewness = skew(hist.flatten())

    return mean, std_dev, skewness


# Baca Citra
image = cv2.imread("Tugas/gambar/luffy2.jpeg")

# Ekstraksi ciri color moment
mean, std_dev, skewness = extract_color_moments(image)

print("Color Moment Features:")
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Skewness:", skewness)
