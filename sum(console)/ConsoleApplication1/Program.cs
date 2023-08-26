using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1, num2, result;
            Console.WriteLine("Enter the value of number1:");
            num1 = Convert.ToInt16(Console.ReadLine());
            Console.WriteLine("Enter the value of number2:");
            num2 = Convert.ToInt16(Console.ReadLine());
            result = num1 + num2;
            Console.Write("sum =:");
            Console.WriteLine(result);
            Console.ReadKey();

        }
    }
}
