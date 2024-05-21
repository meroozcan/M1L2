import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre_uzunlugu = int(input("Şifre uzunluğunu giriniz..."))

sifre = ""

for i in range(sifre_uzunlugu):
    sifre = sifre + random.choice(karakterler)

if sifre_uzunlugu < 8:
    print("8 haneli bir şifre oluşturun.")
    break

else:
    print("şifreniz oluşturuldu.")
    
print(sifre)
