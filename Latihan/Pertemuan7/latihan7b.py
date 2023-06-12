import cv2
import numpy as np

image = cv2.imread("Latihan/Gambar/2.jpg")
kernel = np.ones((3, 3), np.float32) / 9
gaussian_blur = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow("Image Original", image)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.waitKey(0)


def lowPassFiltering(img, size):
    h, w = img.shape[0:2]
    h1, w1 = int(h / 2), int(w / 2)
    img2 = np.zeros((h, w), np.uint8)
    img2[
        h1 - int(size / 2) : h1 + int(size / 2), w1 - int(size / 2) : w1 + int(size / 2)
    ] = 1
    img3 = img2 * img
    return img3


def highPassFiltering(img, size):
    h, w = img.shape[0:2]
    h1, w1 = int(h / 2), int(w / 2)
    img[
        h1 - int(size / 2) : h1 + int(size / 2), w1 - int(size / 2) : w1 + int(size / 2)
    ] = 0
    return img
