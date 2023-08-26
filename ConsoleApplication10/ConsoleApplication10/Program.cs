using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication10
{
    class A
    {
        private string name;
        private int marks, uid;

        public int a_uid
        {
            get
            {
                return uid;
            }
            set
            {
                uid = value;
            }
        }

        public string a_name
        {
            get
            {
                return name;
            }
            set
            {
                name = value;
            }
        }

        public int a_marks
        {
            get
            {
                return marks;
            }
            set
            {
                marks = value;
            }
        }
    }

    class Program
    {
        static void Main()
        {
            A a = new A();
            Console.WriteLine("Enter the UID:");
            a.a_uid = Convert.ToInt16(Console.ReadLine());
            if (a.a_uid > 0)
            {
                Console.WriteLine(" !!! Enter uid is  valid"); 
            }
            else
            {
                Console.WriteLine(" !!! Enter uid is not valid");
            }

            Console.WriteLine("Enter the name:");
            a.a_name = Console.ReadLine();
            if (a.a_name != null)
            {

                Console.WriteLine("Your name  :  "+a.a_name);
               
            }

            else
            {
                Console.WriteLine("!!Please enter the name!!");
              
            }
            Console.WriteLine("Enter the marks:");
            a.a_marks = Convert.ToInt16(Console.ReadLine());

            if (a.a_marks > 50)
            {

                Console.WriteLine("Your marks  :  "+a.a_marks);
               
            }
            
            else 
            {
                Console.WriteLine("Your marks is less then 50");
                Console.ReadKey();
               
            }
               
        }
    }


   
    }

