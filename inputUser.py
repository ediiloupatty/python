# input data dari user

# data yang dimasukan pasti string
data = input("Masukan data : ")

print("data = ", data, "type", type(data))

# jika kita ingin mengambil int, maka
data_int = int(input("Masukan data : "))
print("data ", data_int, " type = ", type(data_int))
data_float = float(input("Masukan data : "))
print("data =", data_float, "type = ", type(data_float))

# boolean berbeda buat int dulu baru ke boolean
data_bool = bool(int(input("Masukan data : ")))
print("data = ", data_bool, "type = ", type(data_bool))
