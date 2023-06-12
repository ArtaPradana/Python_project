import cv2

gambar = cv2.imread("Latihan/Gambar/3.jpg")
cv2.imshow("Gambar Asli", gambar)
scale_percent = 60  # percent of original size
width = int(gambar.shape[1] * scale_percent / 100)
height = int(gambar.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(gambar, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
