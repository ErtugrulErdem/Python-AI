############################ KARŞILAŞTIRMA OPERATÖRLERİ ############################

# == : Esittir
# != : Esit degildir
#  > : Buyuktur
#  < : Kucuktur
# >= : Buyuk esittir
# <= : Kucuk esittir

############################ KARŞILAŞTIRMA OPERATÖRLERİ UYGULAMA ############################

# 1) Kullanicidan 2 vizenin %60 ını ve finalin %40 ini alan alarak ortalama hesaplayin ve ortalama 50'den yüksek ise geçti degilse kaldi yazin

# vize1 = int(input("ilk vize notunuz : "))
# vize2 = int(input("ikinci vize notunuz : "))
# final = int(input("final notunuz : "))
# ortalama = (((vize1 + vize2)/2) * 6 / 10) + (final * 4 / 10)
# sonuc = (50 < ortalama)

# print(f"ortalam notunuz : {ortalama} ve sinifi gecme durumunuz {sonuc}")

# 2) Kullani adi ve sifre isteyip dogrulugunu kontrol ediniz

# kullanici = "ertugrul"
# password = "kucuk"
# kullaniciAdi = input("Kullanici adinizi giriniz : ")
# sifre = input("Sifrenizi giriniz : ")
# kontrolKA = (kullanici == kullaniciAdi)
# kontrolS = (password == sifre)
# print(f"kullanici adiniz {kontrolKA} ve sifreniz {kontrolS}")


############################ MANTIKSAL OPERATÖRLER UYGULAMA (AND , OR , NOT )  ############################

# Kullanicidan isim , boy ve kilo bilgilerini alip kilo indekslerini hesaplayiniz

# isim = input("İsminizi giriniz : ")
# boy = float(input("Boyunu giriniz : "))
# kilo = float(input("Kilonuzu giriniz : "))

# indeks = (kilo /(boy * boy))

# zayif = (0 < indeks) and (indeks <= 18)
# normal = (18 < indeks) and (indeks <= 25)
# kilolu = (25 < indeks) and (indeks <= 30)
# obez = (30 < indeks) and (indeks <= 35)

# print(f"Vücut kitle indeksiniz {indeks}, kilo değerlendirmeniz {zayif}")
# print(f"Vücut kitle indeksiniz {indeks}, kilo değerlendirmeniz {normal}")
# print(f"Vücut kitle indeksiniz {indeks}, kilo değerlendirmeniz {kilolu}")
# print(f"Vücut kitle indeksiniz {indeks}, kilo değerlendirmeniz {obez}")


