sehir = "ankara"

sonuc = sehir.upper()
print(sonuc)
print(sehir.endswith("e"))

def selamVer(isim = "ziyaretçi"):
  print("merhaba " + isim)

selamVer("engin")

def selamVer2(isim, soyIsım ="arkadaş"):
  print("merhaba " +isim  + " " + soyIsım)

selamVer2("derin")
selamVer2("engin", "demiroğ")

def dikUcgenAlanıHesapla(a,b):
  return a*b/2

alan = dikUcgenAlanıHesapla(2,3)

print (alan)

dikUcgenAlanıHesapla2 = lambda a,b : a*b/2

print(dikUcgenAlanıHesapla2(2,3))

x = dikUcgenAlanıHesapla2
print(x(4,5))
