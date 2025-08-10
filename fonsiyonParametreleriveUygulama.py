############################ FONKSİYON PARAMETRELERİ ############################

# def islem(x , y , z =0 ):
#     return sum((x , y , z))    # "sum" fonksiyonu toplama işlemini yapar

# print(islem(10 , 23))
# print(islem(10 , 23 , 45))




# def islem(*params):     # "*" fonksiyonu bana birden fazla parametre işlem yapma imkanı sunar
#     print(params)
#     return sum((params))

# print(islem(10 , 23))
# print(islem(10 , 23 , 45))
# print(islem(10 , 23 , 45 , 56))
# print(islem(10 , 23 , 45 , 56 , 3))




# def kullanici(**args):      # "*" farklı veri tipi kullanıldığı için ve tuple olarak gönderilmediği için çift yıldız kullanılır
#     print(type(args))
#     for key , value in args.items():
#         print(key , value)

# kullanici(name = "ertugrul" , age = 23)
# kullanici(name = "ertugrul" , age = 23 , city = "istanbul")
# kullanici(name = "ertugrul" , age = 23 , city = "istanbul" , ID = 324)
# kullanici(name = "ertugrul" , age = 23 , city = "istanbul" , ID = 324 , Phone = 90)




# def islem(a , b , *args , **kwargs):    # birebir eşleşen parametreler ve listeleri simgeler
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)

# islem(2 , 3 , 5 , k1 = "v1" , k2 = "v2")
# print(islem)




############################ FONKSİYOn UYGULAMALARI ############################

### Gönderilen bir kelimeyi belirten kez ekranda yazdıran bir fonksiyon yazınız

# def yazdir(kelime , tekrar):
#     return kelime * tekrar
# x = yazdir("merhaba\n" ,10)
# print(x)




### Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyon yazınız

# def tamBolen(sayi):
#     bolenler = []

#     for i in range(2,sayi):
#         if sayi % i == 0:
#             bolenler.append(i)
#     return(bolenler)

# print(tamBolen(30))




### Gönderilen iki sayı arasındaki tüm asal sayıları bulan bir fonksiyon yazınız


sayi1 = int(input("sayi1: "))
sayi2 = int(input("sayi2: "))

def asalSayi(sayi1 , sayi2):
    for sayi in range(sayi1 , sayi2+1):
        if sayi > 1:
            for i in range (2,sayi):
                if sayi % i == 0:
                    break
            else:
                print(sayi)

asalSayi(sayi1 , sayi2)