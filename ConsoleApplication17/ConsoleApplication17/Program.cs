using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace ConsoleApplication17
{
    class Program
    {
        class writeFile
        {
            public void Data()
            {

                  StreamWriter sw = new StreamWriter("D:\\practices\\abc.txt");
                  Console.WriteLine("Enter the text that you want to add to you file");
                  String s=Console.ReadLine();
                  sw.WriteLine(s);
                  sw.Flush();
                  sw.Close();
                  Console.WriteLine("The text that you Entered is::::::::");
                  StreamReader sr = new StreamReader("D:\\practices\\abc.txt");
                  {
                      string line;
                      
                      while ((line = sr.ReadLine()) != null)
                      {
                          Console.WriteLine(line);
                      }
                  }
                  Console.WriteLine("Press any key for exit");

            }
        }
        static void Main(string[] args)
        {
           //File.Create(@"D:\practices\abc.txt");
            writeFile wf =new writeFile();
            wf.Data();
            Console.ReadKey();
        }
    }
}
