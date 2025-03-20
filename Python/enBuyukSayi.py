sayi1 = int(input("1. Sayı :"))
sayi2 = int(input("2. Sayı :"))
sayi3 = int(input("3. Sayı :"))

if (sayi1>=sayi2) and (sayi1>=sayi3):
    enBuyuk = sayi1
elif (sayi2>=sayi1) and (sayi2>=sayi3):
    enBuyuk = sayi2
else:
    enBuyuk = sayi3
    
print("En Büyük :",enBuyuk)


ya da

sayi1 = int(input("1. Sayı :"))
sayi2 = int(input("2. Sayı :"))
sayi3 = int(input("3. Sayı :"))
sayilar = [sayi1,sayi2,sayi3]
enBuyuk = sayi1

sayi in sayilar:
for sayi in sayilar:
    if sayi > enBuyuk:
        enBuyuk = sayi
    
print("En Büyük :",enBuyuk)
