using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace leap_year
{
    class Program
    {
        static void Main(string[] args)
        {
            int year;
            Console.WriteLine("Enter the year here::::");
            year = Convert.ToInt16(Console.ReadLine());

            if (year%4==0 && year%400==0)
            {
                Console.WriteLine("Year is leap");
                Console.ReadKey();

            }

            else
            {
                Console.WriteLine("Year is not a leap");
                Console.ReadKey();
            }
            if (year % 4 == 0)
            {
                
                if (year % 100 == 0)
                {
                    if (year % 400 == 0)
                    {
                        Console.WriteLine("Year is leap");
                        Console.ReadKey();
                    }
                    else
                    {
                        Console.WriteLine("Year is not a leap");
                        Console.ReadKey();
                    }
                }
                else
                   {
                      Console.WriteLine("Year is leap");
                      Console.ReadKey();
                   }
            }
            else
            {
                 Console.WriteLine("Year is not a leap");
                 Console.ReadKey();
            }

                
        }
    }
}
