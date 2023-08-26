using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication7
{
    class A
    {
        private int num;

        public int num1
        {
            get
            {
                return num;
            }
            set
            {
                num = value;
            }
        }



        class Program
        {
            static void Main(string[] args)
            {
                A obj1 = new A();
                obj1.num = Convert.ToInt32(Console.ReadLine());
                if (obj1.num % 2 == 0)
                {
                    Console.WriteLine("even");
                    Console.ReadKey();

                }
               
                else
                {
                    Console.WriteLine("odd");
                    Console.ReadKey();
                }



            }
        }
    }
}
