# operasi komparasi
# setiap hasil dari operasi komparasi adalah boolean
# (<,>,<=,>=,==,!=,is,is not)

a = 4
b = 2

print("=== kurang dari (<)")
hasil = a < 4
print(a, "<", 4, "=", hasil)
hasil = b < 4
print(b, "<", 4, "=", hasil)

print("=== lebih dari (>)")
hasil = a > 4
print(a, ">", 4, "=", hasil)
hasil = b > 4
print(b, ">", 4, "=", hasil)

print("=== kurang dari sama dengan (<=)")
hasil = a <= 4
print(a, "<=", b, "=", hasil)
hasil = b <= 4
print(b, "<=", b, "=", hasil)

print("=== lebih dari sama dengan (>=)")
hasil = a >= 4
print(a, ">=", 4, "=", hasil)
hasil = b >= 4
print(b, ">=", 4, "=", hasil)

print("=== sama dengan (==)")
hasil = a == 4
print(a, "==", 4, "=", hasil)
hasil = b == 4
print(b, "==", 4, "=", hasil)

print("=== tidak sama dengan (!=)")
hasil = a != 4
print(a, "=", 4, "=", hasil)
hasil = b != 4
print(b, "=", 4, "=", hasil)

# is, is not sebagai object identity
print("=== object identity (is)")
x = 5
y = 5
print("nilai x =", x, "id =", hex(id(x)))
print("nilai y =", y, "id =", hex(id(y)))
hasil = x is y
print("x is y =", hasil)

x = 5
y = 6
print("nilai x =", x, "id =", hex(id(x)))
print("nilai y =", y, "id =", hex(id(y)))
hasil = x is y
print("x is y =", hasil)

print("=== object identity (is not)")
x = 5
y = 5
print("nilai x =", x, "id =", hex(id(x)))
print("nilai y =", y, "id =", hex(id(y)))
hasil = x is not y
print("x is not y =", hasil)

x = 5
y = 6
print("nilai x =", x, "id =", hex(id(x)))
print("nilai y =", y, "id =", hex(id(y)))
hasil = x is not y
print("x is not y =", hasil)
