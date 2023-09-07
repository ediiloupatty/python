a = 5

print("nilai : ",a)

a += 1
print('nilai a + 1 menjadi : ',a)

a -= 2
print('nilai a - 2 menjadi : ',a)

a *=5
print('nilai a * 5 menjadi : ',a)

a /=2
print ('nilai a / 2 menjadi : ',a)


#modulus dan floor division
b = 10 
print('\nnilai b : ',b)
print('nilai b % 3 : ',b)

b //= 3
print('nilai b //= 3 : ',b)

c = 5
print('nilai c : ',c)

#pangkat
c**=3
print('nilai 3 **3 : ',c)

#operasi bitwise
#OR
d = True
print('\nnilai d : ',d)
d |= False
print('nilai d |= false : ',d)
d = False
print('nilai d : ',d)
d |= False
print('nilai d |= false : ',d)

#AND
d = True
print('\nnilai d : ',d)
d &= False
print('nilai d &= false : ',d)
d = True
print('nilai d : ',d)
d &= True
print('nilai d &= True : ',d)

#XOR
d = True
print('\nnilai d : ',d)
d ^= False
print('nilai d ^= false : ',d)
d = True
print('nilai d : ',d)
d ^= True
print('nilai d ^= True : ',d)

#Geser - geser
e = 0b0100
print('nilai e : ',format(e,'04b'))

e >>=2
print('nilai e >>=2 : ',format(e,'04b'))

e = 0b0100
e <<=1
print('nilai e <<=1 : ',format(e,'04b'))