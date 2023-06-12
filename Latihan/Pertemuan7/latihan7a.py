import cv2
import numpy as np

image = cv2.imread("Latihan/Gambar/2.jpg")
kernel = np.ones((3, 3), np.float32) / 9
processed_image = cv2.filter2D(image, -1, kernel)
mean_blur = cv2.blur(image, (5, 5))
cv2.imshow("Image Original", image)
cv2.imshow("Mean Filter Processing", processed_image)
cv2.imshow("Mean Blur", mean_blur)
cv2.waitKey(0)
