#date and time

import datetime

print("silahkan masukan tanggal, bulan dan, tahun lahir anda :")
tanggal = int(input("tanggal \t: "))
bulan = int(input("bulan \t\t: "))
tahun = int(input("tahun \t\t: "))

tanggal_lahir = datetime.date(tahun,bulan,tanggal)
print(f"anda lahir pada : {tanggal_lahir}")
print(f"harinya adalah \t: {tanggal_lahir:%A}")

hari_ini = datetime.date.today()
print(f"hari ini tanggal : {hari_ini}")
umur = hari_ini - tanggal_lahir
print(f"umur anda adalah : {umur}")
jumlah_tahun = umur.days // 365
print(f"anda sudah berusia : {jumlah_tahun} tahun")