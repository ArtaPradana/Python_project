# Beberapa tipe data lain pada Python
# tipe data boolean
trueOrFalse = True
print(trueOrFalse)
# tipe data array/list
ar = ["blue", "green", "red"]
print(ar[0])  # array pada Python dimulai dari urutan nol (0)
# tipe data dictionary
dic = {
    "nama buah": "durian",
    "nama ilmiah": "Durio Zibethinus",
    "asal": "Malaysia",
    "persebaran": "Asia Tenggara",
}
print(dic["nama buah"])


# pernyataan kondisional
if 5 > 2:
    print("lima lebih dari dua lho")
# operand (operasi pengujian) untuk persamaan menggunakan dua tanda samadengan ('==')
x = 4
y = 8 - x
if x == y:
    print("x dan y sama")
else:
    print("x dan y beda")
# contoh iterasi. cell di atas (no. 9) harus dijalankan terlebih dahulu
# agar variabel 'ar' didefinisikan
for isi in ar:
    print(isi)
