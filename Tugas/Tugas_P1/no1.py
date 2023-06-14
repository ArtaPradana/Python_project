import cv2

img = cv2.imread("Tugas/gambar/luffy1.jpg")


def histogram(Image, n_gray_level):
    Hist = [0] * n_gray_level

    for i in range(Image.shape[0]):
        for j in range(Image.shape[1]):
            gray_level = Image[i][j][0]
            Hist[gray_level] += 1

    n = Image.shape[0] * Image.shape[1]

    for i in range(n_gray_level):
        Hist[i] /= float(n)
        print("Hist[{}] = {}".format(i, Hist[i]))

    return Hist


histogram(img, 256)
