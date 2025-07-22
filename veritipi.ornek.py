"""
x = input("sayi1 :") 
y = input("sayi2 :")

toplam = x + y

print(toplam)
->>string gelir ve çikti 35 gelir
"""
"""
x = int(input("sayi1 :"))
y = int(input("sayi2 :"))

toplam = x + y

print(toplam)
->>x ve y değeri integer tipe dönüşür cevap olarak 3 + 5 = 8 gelir
"""
""" 
x = input("sayi1 :") 
y = input("sayi2 :")

toplam = int(x) + int(y)

print(toplam)
->x ve y değeri string olarak kalir fakat toplam değeri integer tipine dönüşür 10 gelir
"""

########################################################################################################################################
# x = 2                       #integer
# y = 4.5                     #float
# isim = "ertugrul"           #str
# ogrenci = True              #bool

# print(type(x))
# print(type(y))
# print(type(isim))
# print(type(ogrenci))
########################################################################################################################################
                            #VERİ DONUSUMU#
# int to folat
# x = float(5)
# print(x)
# print(type(x))

# float to int
# x = int(4.5)
# print(x)
# print(type(x))

# bool to int
# isim = int(True)
# print(isim)
# print(type(isim))


import math

r = float(input("Dairenin yaricapini giriniz: "))

alan = math.pi * r * r
cevre = 2 * math.pi * r

print("Dairenin alani: ", alan)
print("Dairenin cevresi: ", round(cevre, 5))