// Soyut (abstract) bir sınıf tanımlıyoruz
abstract class Hayvan {
    // Her hayvanın bir ismi vardır
    String isim;

    // Kurucu metod (constructor)
    Hayvan(String isim) {
        this.isim = isim;
    }

    // Soyut metot (abstract method) — bu metodu alt sınıflar tanımlamak zorundadır
    abstract void sesCikar();

    // Soyut olmayan, normal bir metot — alt sınıflar isterse override edebilir
    void hareketEt() {
        System.out.println(isim + " hareket ediyor.");
    }
}

// Abstract sınıftan türeyen bir alt sınıf
class Kedi extends Hayvan {

    // Alt sınıf kendi kurucusunu tanımlar ve üst sınıfın kurucusunu çağırır
    Kedi(String isim) {
        super(isim); // üst sınıfın constructor'ına isim gönderilir
    }

    // Abstract metodu override etmek ZORUNLUDUR
    @Override
    void sesCikar() {
        System.out.println(isim + " miyavlıyor.");
    }
}

// Bir başka alt sınıf
class Kopek extends Hayvan {

    Kopek(String isim) {
        super(isim);
    }

    @Override
    void sesCikar() {
        System.out.println(isim + " havlıyor.");
    }
}

// Main sınıfı: program buradan çalıştırılır
public class Main {
    public static void main(String[] args) {

        // Soyut sınıf örneklenemez: şu şekilde hata verir: new Hayvan("Anonim");
        // Bunun yerine alt sınıf örnekleri oluşturulur

        Hayvan kedi = new Kedi("Minnak");
        Hayvan kopek = new Kopek("Karabas");

        // Ortak metotlar soyut sınıftan miras alınır
        kedi.hareketEt();  // Minnak hareket ediyor.
        kedi.sesCikar();   // Minnak miyavlıyor.

        kopek.hareketEt(); // Karabas hareket ediyor.
        kopek.sesCikar();  // Karabas havlıyor.
    }
}
