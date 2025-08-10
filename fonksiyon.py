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




def yasHesapla(dogumYili):
    return (2025 - dogumYili)
# result = yasHesapla(2002)
# print(result)




def emeklilik(dogumYili , isim):
    yas = yasHesapla(dogumYili)
    emeklilikYasi = 65 - yas
    
    if emeklilikYasi > 0: 
        print(f"{isim} Emekliligine {emeklilikYasi} yil kaldi! ")   
    else:
        print(f"{isim} Emeklisin! ")
    
emeklilik(2002 , "Ertugrul")