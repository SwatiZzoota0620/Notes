using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace divisible
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
                Console.WriteLine("###########Enter the number you want to find number is divisible by 5 and 11 or not##########");
                obj1.num = Convert.ToInt32(Console.ReadLine());
                if (obj1.num % 5 == 0 && obj1.num % 11 == 0)
                {
                    Console.WriteLine(obj1.num+" is divisible by 5 and 11");
                    
                }

                else
                {
                    Console.WriteLine(obj1.num+" is not divisible by 5 and 11");
                   
                }
                Console.WriteLine("Press ENTER  to @@@EXIT@@@");
                Console.ReadKey();
            }
        }
    }
}
