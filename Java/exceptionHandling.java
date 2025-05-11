import java.util.Scanner;

public class ExceptionHandlingExample {
    public static void main(String[] args) {
        // Scanner sınıfı, kullanıcıdan giriş almak için kullanılır
        Scanner scanner = new Scanner(System.in);

        try {
            // try bloğu, hataya sebep olabilecek kodları içerir

            System.out.print("Bir tam sayı girin: ");
            // Kullanıcıdan tam sayı alınır
            int sayi = scanner.nextInt();

            // Eğer kullanıcı geçerli bir sayı girerse bu satır çalışır
            System.out.println("Girdiğiniz sayı: " + sayi);
        } catch (Exception e) {
            // catch bloğu, try içinde oluşabilecek hataları yakalar

            // Eğer kullanıcı geçersiz bir giriş yaparsa (örneğin harf girerse),
            // bu blok çalışır ve hata mesajı verilir
            System.out.println("Hata: Lütfen sadece tam sayı girin.");

            // Hata detaylarını geliştirici için yazdırabiliriz (isteğe bağlı)
            System.out.println("Hata detayları: " + e.getMessage());
        } finally {
            // finally bloğu, hata olsun veya olmasın her zaman çalışır

            // Kaynakları serbest bırakmak için genelde burada kullanılır
            scanner.close();
            System.out.println("Uygulama sonlandı.");
        }
    }
}
