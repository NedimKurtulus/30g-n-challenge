// Arayüz (interface) tanımı
interface Hayvan {
    // Arayüzde sadece metot imzaları (sadece ne yapılacağı belirtilir)
    void sesCikar();  // Her hayvanın bir sesi vardır, ama nasıl çıkardığı sınıfa bağlıdır
    void hareketEt(); // Her hayvan hareket eder, ama nasıl olduğu farklılık gösterir
}

// Arayüzü implemente eden bir sınıf
class Kedi implements Hayvan {
    // Arayüzde tanımlı metotları override (ezmek) zorundayız
    public void sesCikar() {
        System.out.println("Kedi miyavlıyor!");
    }

    public void hareketEt() {
        System.out.println("Kedi sessizce yürüyor.");
    }
}

// Başka bir arayüzü implemente eden sınıf
class Kopek implements Hayvan {
    public void sesCikar() {
        System.out.println("Köpek havlıyor!");
    }

    public void hareketEt() {
        System.out.println("Köpek koşuyor.");
    }
}

// Main sınıfı
public class InterfaceOrnek {
    public static void main(String[] args) {
        // Arayüz tipinde referans ile nesneleri çağırabiliriz
        Hayvan h1 = new Kedi();
        Hayvan h2 = new Kopek();

        // Metotları çağırıyoruz
        h1.sesCikar();    // Kedi miyavlıyor!
        h1.hareketEt();   // Kedi sessizce yürüyor.

        h2.sesCikar();    // Köpek havlıyor!
        h2.hareketEt();   // Köpek koşuyor.
    }
}
