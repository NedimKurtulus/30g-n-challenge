import java.util.Scanner;

public class StringIslemleri {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Bir metin girin: ");
        String girilenMetin = scanner.nextLine();

        // 1. Metni ters çevirme
        String tersMetin = new StringBuilder(girilenMetin).reverse().toString();
        System.out.println("Ters hali: " + tersMetin);

        // 2. Sesli harf sayma
        int sesliHarfSayisi = 0;
        String sesliHarfler = "aeiouAEIOU";
        for (int i = 0; i < girilenMetin.length(); i++) {
            if (sesliHarfler.indexOf(girilenMetin.charAt(i)) != -1) {
                sesliHarfSayisi++;
            }
        }
        System.out.println("Sesli harf sayısı: " + sesliHarfSayisi);

        // 3. Palindrom kontrolü
        if (girilenMetin.equalsIgnoreCase(tersMetin)) {
            System.out.println("Bu metin bir palindromdur.");
        } else {
            System.out.println("Bu metin bir palindrom değildir.");
        }

        // 4. Metni büyük harfe çevirme
        System.out.println("Büyük harfli hali: " + girilenMetin.toUpperCase());
    }
}
