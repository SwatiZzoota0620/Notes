using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication11
{
    public class sample<T>
    {
        T[] obj= new T[5];
        int count = 0;

        public void Add(T item)
        {
            if (count<6)
            {
                obj[count]=item;
            }
            count++;
        }
        public T this[int index]
        {
            get
            {
                return obj[index];
            }
            set
            {
                obj[index]=value;
            }
        }
    }
    class Program
    {
        static void Main(String[] args)
        {
            sample<int> intObj=new sample<int>();
            intObj.Add(5);
            intObj.Add(6);
            intObj.Add(7);
            intObj.Add(8);
            intObj.Add(9);

        for(int i=0; i<5; i++)
        {
        Console.WriteLine(intObj[i]);
        }
        Console.ReadKey();
        
    }
        }
    }

