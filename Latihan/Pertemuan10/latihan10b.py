import cv2
import numpy as np
from matplotlib import pyplot as plt
from cv2 import waitKey
img = cv2.imread('Latihan/Gambar/5.jpg')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
result = cv2.dilate(img, kernel)
cv2.imshow('image asal', img)
cv2.imshow('image hasil', result)
waitKey(0)