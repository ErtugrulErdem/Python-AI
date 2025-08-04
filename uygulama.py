### SAYI TAHMIN OYUNU ###
# 1 - 10 arası rastgele üretilecek olan bir sayıyı yukarı aşağı ifadeleri ile yönlendirerek tahmin edilen sayıyı buldurmak için bir oyun yapın.
# Kullanıcıdan hak bilgisi alarak sayıyı kaç hakta bilmesini istediğini sorun ve can sayısı üzerinden puanını hesaplayın.
# Rastgele sayılar için random() modülünü kullanın.

import random
sayi = random.randint(1,10)
can = int(input("Kaç deneme hakki istersiniz: "))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmininiz: "))
    if tahmin == sayi:
        print(f"Tebrikler {sayac}. denemenizde sayiyi bildiniz ve puaniniz {100 - ((100/can)*(sayac-1))} ")
        break
    elif tahmin > sayi: 
        print("Daha küçük bir sayi tahmin ediniz")
    else:
        print("Daha büyük bir sayi tahmin ediniz")

if hak == 0:
    print(f"Hakkiniz bitmistir ve doğru sayi: {sayi}")

