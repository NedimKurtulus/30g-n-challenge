import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TrafikLambasi extends JPanel implements ActionListener {

    private static final int KIRMIZI = 0;
    private static final int YESIL = 1;
    private static final int SARI = 2;

    private int aktifIsik = KIRMIZI;
    private Timer timer;

    public TrafikLambasi() {
        // Işık değişim süresi: 1000 = 1 saniye
        timer = new Timer(1000, this);
        timer.start();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Arka plan ve çerçeve
        g.setColor(Color.DARK_GRAY);
        g.fillRect(100, 50, 100, 260);

        // Kırmızı ışık
        g.setColor(aktifIsik == KIRMIZI ? Color.RED : Color.GRAY);
        g.fillOval(120, 60, 60, 60);

        // Yeşil ışık
        g.setColor(aktifIsik == YESIL ? Color.GREEN : Color.GRAY);
        g.fillOval(120, 140, 60, 60);

        // Sarı ışık
        g.setColor(aktifIsik == SARI ? Color.YELLOW : Color.GRAY);
        g.fillOval(120, 220, 60, 60);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        // Işık geçişleri
        if (aktifIsik == KIRMIZI) {
            aktifIsik = YESIL;
            timer.setDelay(3000);  // Yeşil 3 saniye
        } else if (aktifIsik == YESIL) {
            aktifIsik = SARI;
            timer.setDelay(1000);  // Sarı 1 saniye
        } else if (aktifIsik == SARI) {
            aktifIsik = KIRMIZI;
            timer.setDelay(3000);  // Kırmızı 3 saniye
        }

        repaint();  // Ekranı yeniden çiz
    }

    public static void main(String[] args) {
        JFrame pencere = new JFrame("Trafik Lambası");
        TrafikLambasi panel = new TrafikLambasi();

        pencere.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        pencere.setSize(320, 400);
        pencere.add(panel);
        pencere.setVisible(true);
        pencere.setLocationRelativeTo(null);
    }
}
