using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication6
{
    class Program
  {
    private int rollno;
    private string name;
    public void Display()
    {
        Console.Write("The Roll No of the student=" + rollno);
        Console.Write("The name of the student=" + name);
        Console.ReadKey();
    }
}

    class displayVariable
{
        static void Main(string[] args)
        {
            Program obj1 = new Program();
            obj1.rollno = 10;
            obj1.name = "swati";
            obj1.Display();  
        }
    }
}

