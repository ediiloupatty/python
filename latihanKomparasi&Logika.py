# membuat gabungan area rentan dari angka

# membuat rentan are kurang dari angka

# ++++++3-------10++++++

inputUser = float(input("masukan angka yang bernilai kurang dari 3\natau\nlebih dari 10 :"))

#+++++++3-------
#memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari 3: ",isKurangDari)

#--------10+++++++
#memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("kurag dari 10 : ",isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan : ",isCorrect)


#-----3++++++10-----
inputUserr = float(input("masukan nilai lebih dari 3\ndan\nkurang dari 10 :"))

isLebihDari = (inputUserr > 3)
print("lebih dari 3 : ",isLebihDari)

isKurangDari = (inputUserr < 10)
print("kurang dari 10",isKurangDari)

isCorrect = isKurangDari and isLebihDari
print(isCorrect)

#PR

#-----0+++++5-----8+++++11-----
inputUser = float(input("masukan angka lebih dari 0 dan kurang dari 5.\nlebih dari 8 dan kurang dari 11 : "))

isLebihDari = (inputUser > 0 and inputUser > 8)
print("lebih dari 0 & 8 : ",isLebihDari)

isKurangDari = (inputUser < 5 and inputUser <11)
print("kurang dari 5 & 11 : ",isKurangDari)

isCorrect = isKurangDari or isLebihDari
print(isCorrect)