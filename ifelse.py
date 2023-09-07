print("silahkan pilih pesanan")
print("1. lemon tea\n2. Es jeruk\n3. jus alvokat")
print("Toping\n")
print("A. less sugar\nB. Ice sugar")

minum = int(input("silahkan pilih : "))
toping = input("silahkan memilih toping : ")

if minum == 1 :
    print("anda memilih lemon tea")
    if toping == 'A' :
        print("Anda memilih les sugar")
    elif toping == 'B' :
        print("anda memilih toping Ice sugar")
elif minum == 2 :
    print("anda memilih es jerus")
elif minum == 3 :
    print("anda memilih jus alvokat")
else :
    print("pilihan anda diluar jangkauan kami. Terimakash:)")