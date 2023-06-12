import cv2
import numpy as np
from matplotlib import pyplot as plt
from cv2 import waitKey


def gammaCorrection(image, gamma=0.5):
    invGamma = 1.0 / gamma
    table = np.array(
        [((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]
    ).astype("uint8")
    return cv2.LUT(image, table)


img = cv2.imread("Latihan/Gambar/2.jpg")
gammaImg = gammaCorrection(img, 2.2)
cv2.imshow("Original image", img)
cv2.imshow("Gamma corrected image", gammaImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
