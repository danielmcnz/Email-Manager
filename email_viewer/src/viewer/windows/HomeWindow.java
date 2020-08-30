package viewer.windows;

import viewer.utils.EMLReader;

public class HomeWindow {
    public HomeWindow()
    {}

    public void ShowEmail()
    {
        EMLReader emlReader = new EMLReader("D:\\git_projects\\Covid 19 and paddling.eml");
        System.out.println(emlReader.Sender());
        System.out.println(emlReader.Recipient());
        System.out.println(emlReader.Subject());
        System.out.println(emlReader.Body());
    }
}