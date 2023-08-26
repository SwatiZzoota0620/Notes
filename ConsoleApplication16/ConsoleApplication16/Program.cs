using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication16
{
    class A
    {
        private char ch;

        public char ch1
        {
            get
            {
                return ch;
            }
            set
            {
                ch = value;
            }
        }

        class Program
        {
            static void Main(string[] args)
            {
                A obj1 = new A();
                Console.WriteLine("Please Enter any character ");
                obj1.ch = Convert.ToChar(Console.ReadLine());

                if ((obj1.ch >= 'a' && obj1.ch <= 'z') || (obj1.ch >= 'A' && obj1.ch <= 'Z'))
                {
                    Console.WriteLine("###Entered character is Alphabet####");
                    if (obj1.ch == 'a' || obj1.ch == 'e' || obj1.ch == 'i' || obj1.ch == 'o' || obj1.ch == 'u' || obj1.ch == 'A' || obj1.ch == 'E' || obj1.ch == 'I' || obj1.ch == 'O' || obj1.ch == 'U')
                    {
                        Console.WriteLine("!!!!! Entered alphabet is VOWEL !!!! ");
                    }
                    else
                    {
                        Console.WriteLine("!!!! Entered alphabet is CONSONANT!!!! ");
                    }

                }
                else if (obj1.ch >= '0' && obj1.ch <= '9')
                {
                    Console.WriteLine("##### Entered character is  integer####");
                }
                else
                {
                    Console.WriteLine("#### Entered character is special character ####");

                }
                Console.ReadKey();
                
            }
        }
    }
}
