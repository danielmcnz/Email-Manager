package viewer.utils;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class EMLReader {
    private String filename;

    private String subject, sender, recipient, body;
    private String boundary = "--00000000000079519805add50e0d";

    public EMLReader(String filename)
    {
        this.filename = filename;
        OpenFile();
    }

    private void OpenFile()
    {
        File file = new File(filename);
        BufferedReader br;
        try
        {
            br = new BufferedReader(new FileReader(file));
            
            String str;
            while((str = br.readLine()) != null)
            {
                if(str.startsWith("Return-Path:"))
                {
                    str = str.split("<")[1];
                    this.recipient = str.split(">")[0];
                }
                else if(str.startsWith("Delivered-To:"))
                {
                    this.sender = str.split(": ")[1];
                }
                else if(str.startsWith("Subject:"))
                {
                    this.subject = str.split(": ")[1];
                }
                else if(str.contains(boundary))
                {
                    // str = br.readLine();
                    // while(str != null)
                    // {
                    //     if(str == boundary)
                    //     {
                    //         //break;
                    //     }
                    //     body += str + "\n";
                    // }
                }
            }
        }
        catch(IOException e)
        {
            System.out.println("buffered reading error in EMLReader");
        }
    }

    public String Subject()
    {
        return this.subject;
    }

    public String Sender()
    {
        return this.sender;
    }

    public String Recipient()
    {
        return this.recipient;
    }

    public String Body()
    {
        return this.body;
    }
}