import numpy as np
import cv2
import matplotlib.pyplot as plt


def perform_kmeans_segmentation(image, num_clusters):
    pixels = image.reshape(-1, 3).astype(np.float32)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    flags = cv2.KMEANS_RANDOM_CENTERS

    _, labels, centers = cv2.kmeans(pixels, num_clusters, None, criteria, 10, flags)

    segmented_image = centers[labels.flatten()].reshape(image.shape)

    return segmented_image


image = cv2.imread("Tugas/gambar/luffy3.jpg")

# Mengubah citra menjadi RGB (jika dalam format BGR)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Normalisasi nilai piksel ke rentang 0-1
normalized_image = image_rgb / 255.0

# Segmentasi citra dengan jumlah kluster yang berbeda
num_clusters = [2, 3, 5, 7]
segmented_images = []
for k in num_clusters:
    segmented_image = perform_kmeans_segmentation(normalized_image, k)
    segmented_images.append(segmented_image)


titles = [
    "Segmentation IMG (2 clusters)",
    "Segmentation IMG (3 clusters)",
    "Segmentation IMG (5 clusters)",
    "Segmentation IMG (7 clusters)",
]
fig, axes = plt.subplots(1, len(segmented_images) + 1, figsize=(12, 4))

axes[0].imshow(image_rgb)
axes[0].set_title("Original Image")
axes[0].axis("off")

for i, seg_image in enumerate(segmented_images):
    axes[i + 1].imshow(seg_image)
    axes[i + 1].set_title(titles[i])
    axes[i + 1].axis("off")

plt.tight_layout()
plt.show()
