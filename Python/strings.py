mesaj = "Kendimi asmak istiyorum"
print(mesaj[2:5])
yeniMesaj = mesaj[12:13]
print(yeniMesaj)

# length

print(len(mesaj))
yeniMesaj = mesaj[len(mesaj)-1:len(mesaj)]
print(yeniMesaj)

#lower upper

print(mesaj.upper())
print (mesaj.lower())

#replace

mesaj = mesaj.replace("ü" , "u")
print(mesaj.replace("a" , "e"))

#split ve strip

bilgi = " Nedim;Kurtuluş;30;Razgrad "  
print(bilgi.split())
print("adı : " + bilgi.split(";")[0])
print(bilgi.strip())

#input

ad = input("Adınız : ")
sayi1 = input("Sayi1 :")
sayi2 = input("Sayi2 :")
print(int(sayi1) + int(sayi2))
