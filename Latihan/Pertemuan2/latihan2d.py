# fungsi datetime dinamakan sebagai 'dt' untuk menyingkat pemanggilan
import datetime as dt

# memanggil fungsi datetime.now pada modul datetime
x = dt.datetime.now()
print(x)
# memanggil hanya fungsi tertentu pada satu modul
from datetime import date

hariIni = date.today()
print("Hari ini tanggal: ", hariIni)
