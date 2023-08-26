using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication3
{
    public class student
    {
        private int sid;
        private string sname;
        public int pid
        {
            set
            {
                sid = value;
            }
            get
            {
                return sid;
            }
        }
        public string pname
        {
            set
            {
                sname = value;
            }
            get
            {
                return sname;
            }
        }
        class Program
        {
            static void Main(string[] args)
        {
            student s1=new student();
            s1.pid=101;
            s1.pname="swati";
            Console.WriteLine("Sid   {0},sname   {1}", s1.pid, s1.pname);
            Console.ReadKey();

        }
        }
    }
}

