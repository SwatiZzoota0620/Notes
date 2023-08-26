using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace program2
{
    class Program
    {
        public int findmax(int num1, int num2)
        {
            int result;
            if (num1 > num2)
                result = num1;
            else
                result = num2;
            return result;
        }


        static void Main(string[] args)
        {
            int a = 10, b = 20, ret;
            Program n = new Program();
            ret=n.findmax(a,b);
            Console.Write(ret);
            Console.ReadKey();
        }
    }
}
