cumle = "bugun hava çok güzel"

kelimeler = cumle.split()

kelimeler.sort()

print(kelimeler)

for kelime in kelimeler:
  print(kelime)

# efektif interaktif gerçek hayat kodu

def kelime_sirala(cumle):
    kelimeler = cumle.split()
    sirali_kelimeler = sorted(kelimeler)
    return sirali_kelimeler

def main():
    cumle = input("Bir cümle giriniz: ")
    sirali_kelimeler = kelime_sirala(cumle)
    print("Alfabetik sıraya göre sıralanmış kelimeler:", sirali_kelimeler)

if __name__ == "__main__":
    main()
