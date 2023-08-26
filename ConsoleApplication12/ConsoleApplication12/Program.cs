using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication12
{
  
    public class abc<T> { 
    	private T message; 
    	public T value 
    	{ 
    		get
    		{ 
    			return this.message; 
    		} 
    		set
    		{ 
    			this.message = value; 
    		} 
    	} 
    } 

 class Program
    {
       
       static void Main(string[] args) 
    	{ 
    		abc<string> pr = new abc<string>(); 
    		pr.value = "Hello SWATI";    		
    		Console.WriteLine("You entered this text::::::::::::"+pr.value);
            Console.ReadKey();

          }
   
        }
    }
