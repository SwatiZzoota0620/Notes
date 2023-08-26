using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication9
{
    class Program
    {
        static void Main(string[] args)
        {
            int day ;
            Console.WriteLine("enter the number");
            day = Convert.ToInt16(Console.ReadLine());
            switch (day)
            {
                case 1:
                    Console.WriteLine("Monday");
                    Console.ReadKey();
                    break;
                case 2:
                    Console.WriteLine("Tuesday");
                    Console.ReadKey();
                    break;
                case 3:
                    Console.WriteLine("Wednesday");
                    Console.ReadKey();
                    break;
                case 4:
                    Console.WriteLine("Thursday");
                    Console.ReadKey();
                    break;
                case 5:
                    Console.WriteLine("Friday");
                    Console.ReadKey();
                    break;
                case 6:
                    Console.WriteLine("Saturday");
                    break;
                case 7:
                    Console.WriteLine("Sunday");
                    break;
               

            }
        }
    }
}
