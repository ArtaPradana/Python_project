import cv2
import numpy as np

img_Asli = cv2.imread("Tugas/gambar/plat.jpeg")

cv2.imshow("Image Asli", img_Asli)
cv2.waitKey(0)
cv2.destroyAllWindows()


def imgBiner(imageAsli):
    img_Abu = cv2.cvtColor(imageAsli, cv2.COLOR_BGR2GRAY)
    _, img_Binering = cv2.threshold(img_Abu, 150, 255, cv2.THRESH_BINARY)
    cv2.imwrite("Tugas/gambar/binary_result.jpeg", img_Binering)
    cv2.imshow("Binary Image", img_Binering)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img_Binering


img_Binered = imgBiner(img_Asli)


def inverse(img_Binered):
    img_Inverse = cv2.bitwise_not(img_Binered)
    cv2.imshow("Inverse Image", img_Inverse)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img_Inverse


img_Inverted = inverse(img_Binered)


def processing(img_Inverted):
    kernel = np.ones((5, 5), np.uint8)
    img_Opening = cv2.morphologyEx(img_Inverted, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening Image", img_Opening)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img_Opening


img_Opened = processing(img_Inverted)


def croping(img_Opened):
    points = cv2.selectROI(
        "Pilih area yang akan di-crop dan tekan tombol 'Enter' untuk melanjutkan...",
        img_Opened,
        showCrosshair=True,
        fromCenter=False,
    )

    img_Croping = img_Opened[
        points[1] : points[1] + points[3], points[0] : points[0] + points[2]
    ]
    cv2.destroyAllWindows()
    cv2.imshow("Citra yang Dicrop", img_Croping)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img_Croping


img_Croped = croping(img_Opened)
