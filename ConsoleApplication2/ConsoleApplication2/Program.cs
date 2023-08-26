using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace ConsoleApplication2
{
    class Program
    {
        static void Main(string[] args)
        {
           // File.Create(@"D:\practices\abc.txt");
           // File.Copy(@"D:\practices\abc.txt", @"D:\practices2\abc.txt");
            //File.Delete(@"D:\practices2\abc.txt");
           // File.Move(@"D:\practices\abc.txt", @"D:\practices2\abc.txt");
            FileInfo f = new FileInfo(@"D:\practices\abc.txt");
           // f.Create();
            //f.MoveTo(@"D:\practices2\abcd.txt");
            // f.CopyTo(@"D:\practices2\abc.txt");
            f.Delete();
        }
    }
}
