using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication4
{
    class example
    {

        string name;
        example()
        {
            Console.WriteLine("hello");
            Console.ReadLine();
        }
        example(string i)
        {
            Console.WriteLine("HEllo swati");
            Console.ReadLine();
        }

        class Program
        {
            static void Main(string[] args)
            {
               
                example s2 = new example("swati");
              
                
            }
        }
    }
}
