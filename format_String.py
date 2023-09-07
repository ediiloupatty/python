#format string


#contoh generic
#string
nama = "edi"
format_str = f"hello {nama}"
print(format_str)


#boolean
boolean = True
format_str = f"boolean {boolean}"
print(format_str)

#angka
angka = 2001.4
format_str = f"angka = {angka}"
print(format_str)


#bilangan bulat
angka = 12
format_str = f"angka = {angka:d}"
print(format_str)

#bilangan ordo ribuan
angka = 150000000000
format_str = f"angka ribuan/jutaan = {angka:,}"
print(format_str)

#bilangan desimal
angka = 2005.123123
format_str = f"bilangan desimal = {angka:.2f}" #2f ini sesuai dengan ke inginan kita berapa angka di tampilkan di belakang koma
print(format_str)

angka = 2005.123123
format_str = f"leading zero = {angka:010.3f}"
print(format_str)

#menampilkan tanda + / -
angka_minus = -19
angka_plus = 10.1234
angka_minus = f"angka minus = {angka_minus:+d}"
angka_plus = f"angka plus = {angka_plus:+}"
print(angka_minus)
print(angka_plus)

#memformat persentase
persentase = 0.054
format_persen = f"persentase = {persentase:.2%}"
print(format_persen)

harga = 10000
jumlah = 3
fomrmat_string = f"harga total = Rp.{harga*jumlah:,}"
print(fomrmat_string)
