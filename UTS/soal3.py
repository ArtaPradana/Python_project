import cv2

image1 = cv2.imread("UTS/gambar/red.jpg")
image2 = cv2.imread("UTS/gambar/mikey.jpg")

image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

and_image = cv2.bitwise_and(image1_gray, image2_gray)
or_image = cv2.bitwise_or(image1_gray, image2_gray)

cv2.imshow("Hasil Bitwise AND", and_image)
cv2.imshow("Hasil Bitwise OR", or_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
