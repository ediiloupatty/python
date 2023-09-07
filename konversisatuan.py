# Latian konversi satuan temperature

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukan suhu dalam celcius : "))
print("suhu adalah", celcius, "celcius")

# reamur
reamur = (4/5)*celcius
print("suhu dalam reamur adalah ", reamur, "reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah", fahrenheit, "fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelcvin adalah ", kelvin, "kelvin")

# fahrenheit ke kelvin
fahrenheit = float(input("Masukan suhu fahrenheit : "))
print("suhu fahrenheit adalah ", fahrenheit, "fahrenheit")

kelvin = (fahrenheit + 459.67) * 5/9
print("suhu dalam kelvin adalah ", kelvin, "kelvin")

kelvin = float(input("Masukan suhu kelvin :"))
print("suhu kelvin adalah ", kelvin, "kelvin")

fahrenheit = (kelvin*(9/5)) - 459.67
print("suhu dalam fahrenheit adalah ", fahrenheit, "fahrenheit")
