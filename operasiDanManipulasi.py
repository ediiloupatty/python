#1. menyambung string concatenate
nama_pertama = "edi"
nama_tengah = "na"
nama_akhir ="loupatty"

nama_lengkap = nama_pertama+" "+nama_tengah+"'"+nama_akhir
print(nama_lengkap)

#menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari" + nama_lengkap + "=" + str(panjang))

d = "edi"
status = d in nama_lengkap
print("string "+ d +" ada di "+nama_lengkap + " = " + str(status))

d = "e"
status = d not in nama_lengkap
print("string " + d + " tidak ada di " + nama_lengkap + " = " + str(status))

#mengulang string
print("wk "*5)
print(10*"ha ")

#indexing
#mengambil data dari string
print("index ke-0 : "+ nama_lengkap[0])
print("index ke-1 : "+ nama_lengkap[1])
print("index ke-3 : "+ nama_lengkap[2])
print("index ke-(-1) : "+nama_lengkap[-1])
print("index ke-[0:2] : "+nama_lengkap[0:3]) #buat lebih a misal 3 buatkan sampai 4
print("index ke [0,2,4,6]"+nama_lengkap[0:7:2])#0 sampai 7 dengan inkremen 2

#item paling kecil
print("paling kecil : "+ min(nama_lengkap))
#item paling besar
print("paling besar : "+ max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah : "+ str(ascii_code))
data = 118
print("char untuk 118 adalah : "+chr(data))

# 4. operator dalam bentuk method
data = "edi loupatty like you"
jumlah = data.count("t")
print("jumlah dari t pada "+data+" adalah = "+str(jumlah))