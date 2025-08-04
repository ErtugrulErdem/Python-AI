############################BREAK CONTINUE############################

# x = 0
# while x < 5:
#     if x == 3:
#         break
#     x += 1 
#     print(x)

# x = 0
# while x < 5:
#     x += 1 
#     if x == 3:
#         continue
#     print(x)

# isim = "ertugrul kucuk"

# for i in isim:
#     if i == " ":
#         break
#     print(i)

# isim = "ertugrul kucuk"

# for i in isim:
#     if i == " ":
#         continue
#     print(i)

# numbers = [1,2,3,4,5,6]

# for num in numbers:
#     if num == 4:
#         break
#     print(num)

# numbers = [1,2,3,4,5,6]

# for num in numbers:
#     if num == 4:
#         continue
#     print(num)


##### 1-100 arası olan tüm tek sayıları bul ve toplamını hesapla
x = 0
toplam = 0
while x <= 100:
    x += 1
    if(x % 2 == 0):
        continue
    toplam += x
    print(x)
print(toplam)