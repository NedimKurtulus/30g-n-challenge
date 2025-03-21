sayi = int(input("sayi : " ))

faktoriyel = 1

if sayi<0:
  print("nagatif sayıların faktoriyeli hesaplanamaz")
elif sayi==0:
  print("sonuc : 1" ))
else:
  for i in range (1, sayi+1):
    faktoriyel = faktoriye *i
  print("sonuc : " , faktoriyel)
