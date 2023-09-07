
a = 1
b = 6

#bitwise OR (/)
c = a|b
print('\n========OR========')
print('nilai :',a,' ,binary : ',format(a,'08b'))
print('nilai :',b,',binary : ',format(b,'08b'))
print('-------------(|)')
print('nilai :',c,'binary : ',format(c,'08b'))

c = a & b
print('\n========AND=======')
print('nilai :',a,' ,binary : ',format(a,'08b'))
print('nilai :',b,',binary : ',format(b,'08b'))
print('-------------(&)')
print('nilai :',c,'binary : ',format(c,'08b'))

c = a ^ b
print('\n========XOR=======')
print('nilai :',a,' ,binary : ',format(a,'08b'))
print('nilai :',b,',binary : ',format(b,'08b'))
print('-------------(^)')
print('nilai :',c,'binary : ',format(c,'08b'))

c = ~a
print('\n========NOT========')
print('nilai : ',a,'binary : ',format(a,'08b'))
print('-------------(`)')
print('nilai :',c,'binary : ',format(c,'08b'))
print('---------------(^)')
d = 0b00001001
e = 0b11111111
print('nilai : ',d^e,'binary ',format(d^e,'08b'))

c = a >> 1
print('\n========SHIFTING >> ========')
print('nilai : ',a,'binary : ',format(a,'08b'))
print('-------------(`)')
print('nilai :',c,'binary : ',format(c,'08b'))

c = b << 1
print('\n========SHIFTING >> ========')
print('nilai : ',a,'binary : ',format(a,'08b'))
print('-------------(`)')
print('nilai :',c,'binary : ',format(c,'08b'))