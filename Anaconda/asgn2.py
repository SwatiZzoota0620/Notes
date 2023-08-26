'''def sum_positive(listeven):
    Sumeven = 0
    for i in listeven: 
        Sumeven += i  	
    return Sumeven 
list = [] 
size = 0 
size = int(input("Enter the size of list: "))
for i in range(size):
    list.append(int(input("Enter number: ")))
    sublist = []
    for num in list:
        if num >= 0:  	 	
          sublist.append(num)  	 	
          print(num," + ", end = " ")
          if len(list) == 0: 
              print("0") 
          else: 
              print("=",sum_positive(sublist))



str = input("Enter the string : ") 
alphabets = 0 
digits = 0 
spaces = 0 
vowels = 0 
special_character = 0 
str = str.lower() 
for i in range(0, len(str)): 
    if (str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u'): 
        vowels = vowels + 1     
    elif str[i] >= 'a' and str[i] <= 'z':             
        alphabets = alphabets + 1     
    elif str[i] >= '0' and str[i] <= '9':         
        digits = digits + 1     
    elif str[i] == ' ': 
        spaces = spaces + 1     
    else: 
        special_character = special_character + 1 
        print("alphabets : ", alphabets) 
print("Digits: ", digits) 
print("spaces: ", spaces) 
print("Vowels: ", vowels) 
print("special_characters : ", special_character) 

class py_solution:     
    def pow(self, x, n):         
        if x == 0 or x == 1 or n == 1: 
            return x 
        if x == -1:             
             if n % 2 == 0:                 
                 return 1             
             else: 
                return -1         
        if n == 0:             
                return 1         
        if n < 0: 
            return 1 / self.pow(x, -n)         
        val = self.pow(x, n // 2)         
        if n % 2 == 0:             
            return val * val 
        return val * val * x 
 
 
print(py_solution().pow(2, -3)); print(py_solution().pow(3, 5)); 
print(py_solution().pow(100, 0)); 

class A: 
    def __init__(self):        
        print('Initializing: class A') 
 
    def sub_method(self, b):         
        print('Printing from class A:', b)        
class B(A): 
    def __init__(self):         
        print('Initializing: class B') 
        super().__init__() 
 
    def sub_method(self, b): 
        print('Printing from class B:', b) 
        super().sub_method(b + 1) 
class C(B):   
    def __init__(self):         
        print('Initializing: class C') 
        super().__init__() 
 
    def sub_method(self, b): 
        print('Printing from class C:', b) 
        super().sub_method(b + 1) 
if __name__ == '__main__':    
        c = C()
        c.sub_method(1) 
        
class Robot(object):
    counter = 0        
    def __init__(self, name):  	        
        self.name = name 
        def sayHello(self): 
             return "Hi, I am " + self.name  
def Rob_init(self, name):  	    
    self.name = name 
Robot2 = type("Robot2",(), {"counter":0, "__init__": Rob_init,"sayHello": lambda self: "Hi, I am " + self.name})  	 	               	 	                	 	             	                
x	= Robot2("Marvin")  	
print(x.name)          
print(x.sayHello()) 
 
y	= Robot("Marvin")  	
print(y.name)   	
print(y.sayHello())  	
print(x.__dict__)   	
print(y.__dict__) '''
 
 
list = ["#" ,"<" ,"=" ,"%" ,"$" ,"?" ,"@" ,"&" ,"!","="]
def add_digits(num):
 return (num - 1) % 9 + 1 if num > 0 else 0
digit = int(input("Enter number: "))
num = add_digits(digit)
print(list[num])


