public class NotDegerlendirici {
    public static void main(String[] args) {

        int not = 82;  // Bu değeri test için değiştirebilirsin

        // 1. if - else if - else ile geçip geçmediğini bulalım
        if (not >= 90) {
            System.out.println("Tebrikler, mükemmel bir not aldın!");
        } else if (not >= 70) {
            System.out.println("Geçtin, gayet başarılı!");
        } else if (not >= 50) {
            System.out.println("Geçtin ama daha iyi olabilirdi.");
        } else {
            System.out.println("Kaldın, üzülme daha çok çalışabilirsin!");
        }

        // 2. switch-case ile harf notu verelim
        char harfNotu;

        if (not >= 90) {
            harfNotu = 'A';
        } else if (not >= 80) {
            harfNotu = 'B';
        } else if (not >= 70) {
            harfNotu = 'C';
        } else if (not >= 60) {
            harfNotu = 'D';
        } else {
            harfNotu = 'F';
        }

        System.out.println("Harf notunuz: " + harfNotu);

        // 3. switch-case ile harf notuna göre mesaj verelim
        switch (harfNotu) {
            case 'A':
                System.out.println("Mükemmelsin!");
                break;
            case 'B':
                System.out.println("Harika bir başarı!");
                break;
            case 'C':
                System.out.println("Fena değil, ama gelişebilirsin.");
                break;
            case 'D':
                System.out.println("Daha çok çalışmalısın.");
                break;
            case 'F':
                System.out.println("Maalesef kaldın. Yeni bir başlangıç için şansın var.");
                break;
            default:
                System.out.println("Geçersiz harf notu.");
        }
    }
}
