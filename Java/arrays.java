import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Arrays;

public class ArrayExamples {
    public static void main(String[] args) {

        // 1. KLASİK DİZİLER (ARRAYS)
        int[] sayilar = {10, 20, 30, 40, 50};

        System.out.println("Klasik Dizi:");
        for (int i = 0; i < sayilar.length; i++) {
            System.out.println("Index " + i + ": " + sayilar[i]);
        }

        // Dizinin elemanlarını değiştir
        sayilar[2] = 99;
        System.out.println("3. eleman değiştirildi: " + sayilar[2]);

        // 2. ARRAYLIST (DİNAMİK DİZİ BENZERİ)
        ArrayList<String> isimler = new ArrayList<>();
        isimler.add("Ali");
        isimler.add("Veli");
        isimler.add("Ayşe");

        System.out.println("\nArrayList:");
        for (int i = 0; i < isimler.size(); i++) {
            System.out.println("Eleman " + i + ": " + isimler.get(i));
        }

        // Eleman sil ve ekle
        isimler.remove("Veli");
        isimler.add("Zeynep");
        System.out.println("Güncellenmiş ArrayList: " + isimler);

        // 3. LINKEDLIST (LİST YAPISI - SIKI BAĞLI DÜĞÜMLER)
        LinkedList<Double> notlar = new LinkedList<>();
        notlar.add(80.5);
        notlar.add(92.0);
        notlar.add(67.5);

        System.out.println("\nLinkedList:");
        for (double not : notlar) {
            System.out.println("Not: " + not);
        }

        // İlk ve son elemana erişim
        System.out.println("İlk not: " + notlar.getFirst());
        System.out.println("Son not: " + notlar.getLast());

        // 4. DİZİLERDEKİ METODLAR VE ARRAYS SINIFI
        int[] sayilar2 = {5, 2, 9, 1, 7};
        System.out.println("\nDiziyi sıralamadan önce: " + Arrays.toString(sayilar2));
        Arrays.sort(sayilar2);
        System.out.println("Sıralanmış dizi: " + Arrays.toString(sayilar2));

        // 5. DİZİ KOPYALAMA
        int[] kopyaDizi = Arrays.copyOf(sayilar2, sayilar2.length);
        System.out.println("Kopyalanmış dizi: " + Arrays.toString(kopyaDizi));

        // 6. 2 BOYUTLU DİZİLER
        int[][] matris = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        System.out.println("\n2 Boyutlu Dizi (Matris):");
        for (int i = 0; i < matris.length; i++) {
            for (int j = 0; j < matris[i].length; j++) {
                System.out.print(matris[i][j] + " ");
            }
            System.out.println();
        }
    }
}
