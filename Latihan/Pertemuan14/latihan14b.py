import cv2
import os
from xml.dom import minidom
import latihan14c as latihan14c

dir = "Latihan/Pertemuan14/train"

data_training = []
for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    if os.path.isfile(f):
        if filename.endswith(".xml"):
            data = minidom.parse(f)
            items = data.getElementsByTagName("filename")[0]

            hsl = items.firstChild.data
            gambar = dir + "/" + hsl
            kls = data.getElementsByTagName("object")
            target_kls = kls[0].getElementsByTagName("name")[0].firstChild.data
            print(gambar)
            fitur = latihan14c.ekstrak_fitur(gambar)
            data_training.append(fitur)
