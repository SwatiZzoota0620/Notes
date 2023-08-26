using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;


namespace ConsoleApplication19
{
    class Program
    {
        static void Main(string[] args)
        {
            XmlTextReader x = new XmlTextReader("c:\\users\\hp\\documents\\visual studio 2010\\Projects\\ConsoleApplication19\\ConsoleApplication19\\XMLFile1.xml");
            while (x.Read())
            {
                if (x.NodeType == XmlNodeType.Element && x.Name == "NAME")
                {
                    string s1 = x.ReadElementString();

                    Console.WriteLine("name=" + s1);
                }
                if (x.NodeType == XmlNodeType.Element && x.Name == "CLASS")
                {
                    string s2 = x.ReadElementString();
                    Console.WriteLine("class=" + s2);
                }
                Console.ReadKey();

            }
        }
    }
}
