using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication3
{
    public class program
    {
    
        private int rollno;
        private string name;
        public int pid
        {
            set
            {
               rollno = value;
            }
            get
            {
                return rollno;
            }
        }
        public string pname
        {
            set
            {
                name = value;
            }
            get
            {
                return name;
            }
        }
    }
        class student
        {
            static void Main(string[] args)
            {
                program s1 = new program();
                s1.pid = 10;
                s1.pname = "anamika";
                Console.WriteLine("ROLL NO OF STUDENT {0}  ,   NAME OF STUDENT {1}", s1.pid, s1.pname);
                Console.ReadKey();

            }
        }
    
}

