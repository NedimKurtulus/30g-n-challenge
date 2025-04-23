import java.util.Scanner;

public class MatrisToplama {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Matris boyutlarını al
        System.out.print("Satır sayısını girin: ");
        int satir = input.nextInt();

        System.out.print("Sütun sayısını girin: ");
        int sutun = input.nextInt();

        // Matrisleri tanımla
        int[][] matris1 = new int[satir][sutun];
        int[][] matris2 = new int[satir][sutun];
        int[][] toplam = new int[satir][sutun];

        // İlk matrisi kullanıcıdan al
        System.out.println("1. matrisin elemanlarını girin:");
        for (int i = 0; i < satir; i++) {
            for (int j = 0; j < sutun; j++) {
                System.out.print("matris1[" + i + "][" + j + "] = ");
                matris1[i][j] = input.nextInt();
            }
        }

        // İkinci matrisi kullanıcıdan al
        System.out.println("2. matrisin elemanlarını girin:");
        for (int i = 0; i < satir; i++) {
            for (int j = 0; j < sutun; j++) {
                System.out.print("matris2[" + i + "][" + j + "] = ");
                matris2[i][j] = input.nextInt();
            }
        }

        // Matrisleri topla
        for (int i = 0; i < satir; i++) {
            for (int j = 0; j < sutun; j++) {
                toplam[i][j] = matris1[i][j] + matris2[i][j];
            }
        }

        // Sonuç matrisini yazdır
        System.out.println("Toplam matris:");
        for (int i = 0; i < satir; i++) {
            for (int j = 0; j < sutun; j++) {
                System.out.print(toplam[i][j] + "\t");
            }
            System.out.println();
        }
    }
}
