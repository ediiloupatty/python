#width and multiline

#data
data_nama = "edi loupatty"
data_umur = 21
data_tinggi = 152
data_nomor_sepatu = 44

#string
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, no sepatu = {data_nomor_sepatu}"
print(5*"="+"Data string"+5*"=")
print(data_string)

#dengan /n
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nno sepatu = {data_nomor_sepatu}"
print(5*"="+"Data string"+5*"=")
print(data_string)

#dengan kutip triplets
data_string = f"""nama        = {data_nama}
umur        = {data_umur}
tinggi      = {data_tinggi}
no sepatu   = {data_nomor_sepatu}
"""
print(5*"="+"Data string"+5*"=")
print(data_string)

#bisa dibuat rata kanan
data_nama = "edi"
data_string = f"""nama        = {data_nama:>5}
umur        = {data_umur:>5}
tinggi      = {data_tinggi:>5}
no sepatu   = {data_nomor_sepatu:>5}
"""
print(5*"="+"Data string"+5*"=")
print(data_string)