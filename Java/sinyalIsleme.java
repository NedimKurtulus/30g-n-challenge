import java.util.Random;

public class SinyalIsleme {

    public static void main(String[] args) {
        int N = 100; // örnek sayısı
        double[] sinyal = new double[N];
        double[] gürültülüSinyal = new double[N];
        double[] filtreliSinyal = new double[N];
        int pencereBoyutu = 5;

        // 1. Saf sinüs sinyali üret
        for (int i = 0; i < N; i++) {
            sinyal[i] = Math.sin(2 * Math.PI * i / 20); // dalga periyodu = 20
        }

        // 2. Gürültü ekle
        Random rastgele = new Random();
        for (int i = 0; i < N; i++) {
            double gürültü = 0.5 * (rastgele.nextDouble() - 0.5); // -0.25 ile +0.25 arasında gürültü
            gürültülüSinyal[i] = sinyal[i] + gürültü;
        }

        // 3. Hareketli ortalama filtresi uygula
        for (int i = 0; i < N; i++) {
            double toplam = 0;
            int sayac = 0;
            for (int j = i - pencereBoyutu / 2; j <= i + pencereBoyutu / 2; j++) {
                if (j >= 0 && j < N) {
                    toplam += gürültülüSinyal[j];
                    sayac++;
                }
            }
            filtreliSinyal[i] = toplam / sayac;
        }

        // 4. Sonuçları yazdır
        System.out.println("i\tSinüs\tGürültülü\tFiltreli");
        for (int i = 0; i < N; i++) {
            System.out.printf("%d\t%.3f\t%.3f\t\t%.3f\n", i, sinyal[i], gürültülüSinyal[i], filtreliSinyal[i]);
        }
    }
}
