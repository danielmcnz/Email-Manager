package viewer;

import javax.swing.JFrame;
import javax.swing.plaf.DimensionUIResource;

import viewer.windows.HomeWindow;

public class window {
    public static void main(String[] args)
    {
        String TITLE = "Direct Mail";
        int WIDTH = 1350;
        int HEIGHT = 750;

        JFrame frame = new JFrame();
        frame.setTitle(TITLE);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setMinimumSize(new DimensionUIResource(WIDTH, HEIGHT));
        frame.setLocationRelativeTo(null);
        frame.setResizable(false);

        HomeWindow homeWindow = new HomeWindow();
        homeWindow.ShowEmail();
        
        frame.setVisible(true);
    }
}
