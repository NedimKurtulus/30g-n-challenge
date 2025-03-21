x=[[1,2,5],[2,4,1],[1,5,7]]
y=[[3,3,4],[2,4,1],[3,5,4]]

sonuc = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
  for j in range(len(y)):
    sonuc[i][j] = x[i][j]+y[i][j]

print (sonuc)

# gerçek efektif interaktif kod

def matris_olustur(satir, sutun):
    matris = []
    print(f"{satir}x{sutun} boyutunda matrisin elemanlarını giriniz:")
    for i in range(satir):
        satir_elemanlari = []
        for j in range(sutun):
            eleman = int(input(f"Matris[{i}][{j}] = "))
            satir_elemanlari.append(eleman)
        matris.append(satir_elemanlari)
    return matris

def matris_topla(matris1, matris2):
    satir = len(matris1)
    sutun = len(matris1[0])
    toplam_matris = []
    for i in range(satir):
        satir_elemanlari = []
        for j in range(sutun):
            satir_elemanlari.append(matris1[i][j] + matris2[i][j])
        toplam_matris.append(satir_elemanlari)
    return toplam_matris

def matris_yazdir(matris):
    for satir in matris:
        print(" ".join(map(str, satir)))

# Kullanıcıdan satır ve sütun sayısını alma
satir = int(input("Matrisin satır sayısını giriniz: "))
sutun = int(input("Matrisin sütun sayısını giriniz: "))

# İki matris oluşturma
print("Birinci matris:")
matris1 = matris_olustur(satir, sutun)

print("İkinci matris:")
matris2 = matris_olustur(satir, sutun)

# Matrisleri toplama
toplam_matris = matris_topla(matris1, matris2)

# Sonucu ekrana yazdırma
print("Matrislerin toplamı:")
matris_yazdir(toplam_matris)
