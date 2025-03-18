ogrenciler ["engin","derin","salih"]
ogrenciler.append("ahmet")
print(ogrenciler[3])
ogrenciler.remove("salih")
print(ogrenciler)

#list constructor

sehirler = list(("ankara" , "istanbul" , "izmir" ))
print(sehirler)
print(len(sehirler))

#diger fonksiyonlar 

print("ankara sayiyi: "+ str(sehirler.count("ankara")))
print("ankara indexi : " + str(sehirler.index("ankara")))
sehirler.pop(1)
sehirler.insert(0,"istanbul")
sehirler.reverse()
print(sehirler)

sehirler3 = sehirler.copy()
sehirler2=sehirler
sehirler2[0] = "izmir"

print(sehirler2)
print(sehirler)
print(sehirler3)

sehirler.extend(sehirler3)
sehirler.sort()
sehirler.reverse()
print(sehirler)
