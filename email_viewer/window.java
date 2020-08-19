package direct_mail.email_viewer;

import javax.swing.JFrame;
import javax.swing.plaf.DimensionUIResource;

public class window {
    public static void main(String[] args)
    {
        String TITLE = "Direct Mail";
        int WIDTH = 1200;
        int HEIGHT = 800;

        JFrame frame = new JFrame();
        frame.setTitle(TITLE);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setMinimumSize(new DimensionUIResource(WIDTH, HEIGHT));
        frame.setLocationRelativeTo(null);
        
        frame.setVisible(true);
    }
}
