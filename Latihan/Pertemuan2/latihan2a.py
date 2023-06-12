# ini adalah komentar pada baris python
# mencetak ke layar menggunakan perintah 'print'
print("hello world!")
# mendefinisikan variabel
x = 5
y = 6
# operasi artimatika sederhana
hasil = x * y + 2 * x - 2 * y
# mencetak hasil ke keluaran
print("hasil dari operasi adalah", hasil)
# variabel juga dapat didefinisikan sekaligus, dipisahkan oleh tanda koma
var1, var2 = 23.5, "ini adalah isi var2"
print("isi var1: ", var1, "\n isi var2: ", var2)

# Tipe data pada Python didefinisikan pada saat variabel dibuat
x = 5  # int
y = 6.5  # float
z = "bahasa ular"  # str
hasil = x + y  # penjumlahan antara int dan float
print(hasil)  # mencetak hasil
print(type(hasil))  # mencetak tipe data hasil
# cell berikut hanya akan bisa dijalankan
# apabila cell di atas sudah dijalankan sebelumnya

hasil = x + z  # akan muncul error akibat penjumlahan tipe data yang tidak sesuai
