import java.util.Scanner;

public class FırınSimülatörü {
    static int sicaklik = 20;   // Başlangıç sıcaklığı
    static int nem = 0;         // Başlangıç nem (0/1)
    static int tarifSicaklik = 150; // Tarif sıcaklığı
    static int tarifNem = 0;        // Tarif nemi

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.println("\nSıcaklık (0-250): " + sicaklik);
            System.out.println("Nem (0/1): " + nem);
            System.out.println("Menü: 1:+1 2:-1 3:+10 4:-10 n:toggle t:tarif");
            System.out.print("Seçiminiz: ");
            
            String input = scanner.nextLine();
            if (input.isEmpty()) continue;
            char choice = input.charAt(0);

            switch (choice) {
                case '1': inc1(); break;
                case '2': dec1(); break;
                case '3': inc10(); break;
                case '4': dec10(); break;
                case 'n': toggleNem(); break;
                case 't': loadRecipe(); break;
                default: System.out.println("Geçersiz seçim!"); break;
            }
        }
    }

    static void inc1() {
        if (sicaklik < 250) {
            sicaklik++;
        }
    }
    
    static void dec1() {
        if (sicaklik > 0) {
            sicaklik--;
        }
    }
    
    static void inc10() {
        for (int i = 0; i < 10; i++) {
            if (sicaklik < 250) {
                sicaklik++;
            } else {
                break;
            }
        }
    }
    
    static void dec10() {
        for (int i = 0; i < 10; i++) {
            if (sicaklik > 0) {
                sicaklik--;
            } else {
                break;
            }
        }
    }
    
    static void toggleNem() {
        nem = 1 - nem;
    }
    
    static void loadRecipe() {
        sicaklik = tarifSicaklik;
        nem = tarifNem;
    }
}
