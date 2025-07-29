######################  KOŞULLU BLOKLARDA UYGULAMALAR   ################################# 
# 1) Kullaniciya satilan ve kullanima baslanma zamani alinan bir buzdolabinin servis zamanini asagidaki bilgilere göre hesaplayiniz
# 1.bakim : 1.yil
# 2.bakim : 2.yil
# 3.bakim : 3.yil 
# süre hesabini alinan gun ay yil bilgisine gore gun bazli ve 365 gun uzerinden hesaplayiniz


import datetime                                            # zaman ve tarih modülü

tarih = input("Buzdolabini satin alma tarihiniz nedir (1111/11/11) : ")
tarih = tarih.split("/")                                   #split istenilen yerden böler
# print(tarih)
# print(tarih[0])
# print(tarih[1])
# print(tarih[2])
kullanilanZaman = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
canliZaman = datetime.datetime.now()                       #now şimdiki zamanı verir
bakimZamani = canliZaman - kullanilanZaman
gun = bakimZamani.days                                     #.days aradaki zamanın sadece gün farkını verir 
print(gun)

if gun <= 365:
    print("1.bakim sureniz gelmistir")
elif (gun > 365) and  (gun < 365 * 2):
    print("2.bakim sureniz gelmistir")
elif (gun > 365 * 2) and  (gun < 365 * 3):
    print("3.bakim sureniz gelmistir")
else : 
    print("bakim hakki gununuz gecmistir")
