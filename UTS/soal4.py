import cv2

image1 = cv2.imread("UTS/gambar/red.jpg")
image2 = cv2.imread("UTS/gambar/mikey.jpg")

gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

subtracted_image = cv2.subtract(gray2, gray1)
reflected_image = cv2.flip(subtracted_image, 0)

cv2.imshow("Hasil Pengurangan Dan Refleksi", reflected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
