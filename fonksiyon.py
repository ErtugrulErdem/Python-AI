############################ FONKSİYONLAR ############################

# def selamla(kullanici):
#     print(f"merhaba {kullanici}")

# selamla("ertugrul")




# def selamla(kullanici):
#     return(f"merhaba {kullanici}") #return verilen ifadedeki bilgiyi tutar ve geri döndürür.

# mesaj = selamla("ertugrul")
# print(mesaj)




# def toplama(sayi1 , sayi2):
#     return(sayi1 + sayi2)

# result = toplama(15 , 25)
# print(result)




# def yasHesapla(dogumYili):
#     return (2025 - dogumYili)
# # result = yasHesapla(2002)
# # print(result)




# def emeklilik(dogumYili , isim):
#     """
#     docstring = doğum yilinizi girerek emekliliğinize kaç yil kaldigini belirtir
#     input = dogum yili girmenizi bekler
#     output = emeklilik yasinizi verir
#     """
#     yas = yasHesapla(dogumYili)
#     emeklilikYasi = 65 - yas
    
#     if emeklilikYasi > 0: 
#         print(f"{isim} Emekliligine {emeklilikYasi} yil kaldi! ")   
#     else:
#         print(f"{isim} Emeklisin! ")
    
# emeklilik(2002 , "Ertugrul")




############################ LAMBDA FONKSİYONU ############################

# def toplam (x,y):
#     return x+y
# print(toplam(2,5))

# toplam = lambda x,y: x+y

# print(toplam(3,2))




############################ MAP FONKSİYON KOMUTU ############################
### map ve filter komutu nesne olarak yani yapılan işlemin adresini verir listeye çevirirsen sayı olarak değer alırsın 

# def kupAl(sayi):
#     return sayi ** 3

# result = kupAl(4)
# print(result)

# sayilar = [1 , 2, 3]
# result = map(kupAl , sayilar)
# print(result)

# result = [*map(kupAl , sayilar)]
# print(result)

# result = list(map(kupAl , sayilar))
# print(result)

# for result in map(kupAl , sayilar):
#     print(result)




############################ FILTER FONKSİYON KOMUTU ############################
### map ve filter komutu nesne olarak yani yapılan işlemin adresini verir listeye çevirirsen sayı olarak değer alırsın 


# sayilar = [1,2,3,4,5]

# def sayiKontrol(x):
#     return x % 2 == 0    # true veya false çevir

# print(sayiKontrol(5))
# print(sayiKontrol(6))


# result = filter(sayiKontrol , sayilar)
# print(result)

# result = list(filter(sayiKontrol , sayilar))
# print(result)