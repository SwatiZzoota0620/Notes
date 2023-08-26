using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication2
{
    class Program
    {
        static void Main(string[] args)
        {
            int age;
            Console.WriteLine("age:");
            age = Convert.ToInt16(Console.ReadLine());
            if (age >= 13 && age <= 19)
            {
                Console.WriteLine("{0} is teenage", age);
                Console.ReadKey();
            }
            else
            {
                Console.WriteLine("{0} not teenage", age);
                Console.ReadKey();
            }
        }
    }
}
