import cv2
import matplotlib.pyplot as plt

# Membaca gambar sebagai citra grayscale
image = cv2.imread("Tugas/gambar/luffy1.jpg", 0)

# Melakukan thresholding global
_, global_threshold_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Melakukan thresholding Otsu
_, otsu_threshold_image = cv2.threshold(
    image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Menampilkan citra-citra menggunakan matplotlib
fig, axes = plt.subplots(1, 3, figsize=(10, 4))
axes[0].imshow(image, cmap="gray")
axes[0].set_title("Citra Asli")
axes[0].axis("off")
axes[1].imshow(global_threshold_image, cmap="gray")
axes[1].set_title("Thresholding Global")
axes[1].axis("off")
axes[2].imshow(otsu_threshold_image, cmap="gray")
axes[2].set_title("Thresholding Otsu")
axes[2].axis("off")

plt.show()
