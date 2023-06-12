import cv2

image1 = cv2.imread("UTS/gambar/red.jpg", 0)
image2 = cv2.imread("UTS/gambar/mikey.jpg", 0)

subtracted_image = cv2.subtract(image2, image1)

cv2.imshow("Hasil Pengurangan", subtracted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
