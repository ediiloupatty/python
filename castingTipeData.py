# merubah 1 tipe data ke tipe data yang lain
# tipe data = int, float, str, bool


# INTEGER
print("====INTEGER====")
data_int = 9
print("data = ", data_int, ",type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_bool, ",type =", type(data_bool))

# FLOAT
print("====FLOAT====")
data_float = 9.5
print("data = ", data_float, "type =", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_str, "type = ", type(data_str))
print("data = ", data_bool, "type =", type(data_bool))

print("====STRING====")
data_str = "0"
print("data = ", data_str, "type = ", type(data_str))

data_int = int(data_str)
data_float = float(data_str)
# di anggap true karena tidak di anggap int dan float
data_bool = bool(data_str)
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_bool, "type = ", type(data_bool))

# BOOLEAN
print("====BOOLEAN====")
data_bool = True
print("data =", data_bool, "type =", type(data_bool))

data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_str, "type = ", type(data_str))
