// Kapsüllenecek olan sınıf
public class Calisan {

    // 1. Adım: Alanları private yap
    private String isim;
    private int yas;
    private double maas;

    // 2. Adım: Dışarıdan okuma için getter
    public String getIsim() {
        return isim;
    }

    public int getYas() {
        return yas;
    }

    public double getMaas() {
        return maas;
    }

    // 3. Adım: Dışarıdan değer atamak için setter
    public void setIsim(String yeniIsim) {
        this.isim = yeniIsim;
    }

    public void setYas(int yeniYas) {
        if (yeniYas > 0) { // Doğrulama ile kontrol
            this.yas = yeniYas;
        }
    }

    public void setMaas(double yeniMaas) {
        if (yeniMaas >= 8500) { // Asgari sınır kontrolü
            this.maas = yeniMaas;
        }
    }
}
