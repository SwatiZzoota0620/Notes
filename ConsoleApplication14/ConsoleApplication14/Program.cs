using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication14
{
    class postive_or_negative
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
                num= value;
            }
        }
        class Program
        {
            static void Main(string[] args)
            {
                postive_or_negative obj = new postive_or_negative();
                Console.Write("Enter the number here:::::::");
                obj.num = Convert.ToInt32(Console.ReadLine()); ;

                if (obj.num > 0 || obj.num == 0)
                {
                    Console.WriteLine("Number is postive");
                    Console.ReadKey();

                }
                else
                {
                    Console.WriteLine("Number is negative");
                    Console.ReadKey();
                }
            }
        }
    }
}
