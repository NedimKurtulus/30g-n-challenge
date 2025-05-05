public class Main {
    public static void main(String[] args) {
        // Nesne oluştur
        Calisan c1 = new Calisan();

        // Verileri set et
        c1.setIsim("Ahmet Yılmaz");
        c1.setYas(28);
        c1.setMaas(15000);

        // Verileri oku
        System.out.println("İsim: " + c1.getIsim());
        System.out.println("Yaş: " + c1.getYas());
        System.out.println("Maaş: " + c1.getMaas());
    }
}
