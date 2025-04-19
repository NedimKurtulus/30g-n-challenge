import java.util.Scanner;
import javax.script.ScriptEngineManager;
import javax.script.ScriptEngine;

public class GercekHesapMakinesi {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Gerçek hesap makinesine hoş geldin!");
        System.out.println("Lütfen yapmak istediğin işlemi yaz (örn: 5 + 2 * 3 - 4 / 2):");
        System.out.print("İşlem: ");

        String ifade = scanner.nextLine();

        try {
            // Java'da ifade çözümlemek için JavaScript motoru kullanıyoruz
            ScriptEngineManager manager = new ScriptEngineManager();
            ScriptEngine engine = manager.getEngineByName("JavaScript");

            Object sonuc = engine.eval(ifade);

            System.out.println("Sonuç: " + sonuc);
        } catch (Exception e) {
            System.out.println("Hata: Geçersiz işlem. Lütfen matematiksel ifadeyi düzgün gir.");
        }
    }
}
