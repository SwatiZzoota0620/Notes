"""from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("444x500")
root.title("Register Form")
root.configure(bg="blue")
f1=Frame(root, bg="blue")
Label(f1, text="Register !", font="Helvetica 30",fg="white",bg="blue",
pady=30).pack(side=RIGHT)
f1.grid(row=0, column=2, sticky="S")
id = Label(root,text="Id:",font="Helvetica 20",fg="white",bg="blue")
name = Label(root,text="Name:",font="Helvetica 20",fg="white",bg="blue")
designation = Label(root,text="Designation:",font="Helvetica 20",fg="white",bg="blue")
gender=Label(root, text="Gender:",font="Helvetica 20",fg="white",bg="blue")
salary=Label(root, text="Salary:",font="Helvetica 20",fg="white",bg="blue")
id.grid(row=1, column=1, sticky="W")
name.grid(row=2, column=1, sticky="W")
designation.grid(row=3, column=1, sticky="W")
gender.grid(row=4, column=1, sticky="W")
salary.grid(row=5, column=1, sticky="W")
id_value=StringVar()
name_value=StringVar()
designation_value=StringVar()
gender_value=StringVar()
salary_value=IntVar()
id_entry=Entry(root, textvariable=id_value)
name_entry=Entry(root, textvariable=name_value)
designation_entry=Entry(root, textvariable=designation_value)
gender_entry=Entry(root, textvariable=gender_value)
salary_entry=Entry(root, textvariable=salary_value)
id_entry.grid(row=1, column=2)
name_entry.grid(row=2, column=2)
designation_entry.grid(row=3, column=2)
gender_entry.grid(row=4, column=2)
salary_entry.grid(row=5, column=2)
con=mysql.connect(
 host="localhost",
 user="root",
 password="Ubaid@123",
 db="test"
)
mycursur=con.cursor()
def register ():
 id1=id_value.get()
 name1=name_value.get()
 designation1=designation_value.get()
 gender=gender_value.get()
 salary=salary_value.get()
 var=(id1,name1,designation1, gender, salary)
 insert="insert into user values (%s,%s,%s,%s,%s)"
 mycursur.execute(insert, var)
 con.commit()
 id_value.set("")
 name_value.set("")
 designation_value.set("")
 gender_value.set("")
 salary_value.set("0")
def show(event):
 tmsg.showinfo("Alert !","Record Entered.")
button=Button(text="Register", command =register, padx=20)
button.grid(rowspan=6, column=2, pady=10, sticky=NSEW, columnspan=2)
button.bind('<Button-1>',show)
root.mainloop()





from tkinter import Toplevel, Button, Tk, Menu  
  
top = Tk()  
menubar = Menu(top)  
file = Menu(menubar, tearoff=0)  
file.add_command(label="New")  
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as...")  
file.add_command(label="Close")  
  
file.add_separator()  
  
file.add_command(label="Exit", command=top.quit)  
  
menubar.add_cascade(label="File", menu=file)  
edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
  
edit.add_separator()  
    
edit.add_command(label="Redo")  
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
  
menubar.add_cascade(label="Edit", menu=edit)  
help = Menu(menubar, tearoff=0)
help.add_command(label="Myhelp")  
help.add_command(label="About")  
help.add_command(label="Contact")
menubar.add_cascade(label="Help", menu=help)     

  
top.config(menu=menubar)  
top.mainloop()



import random 
from tkinter import *
from tkinter.ttk import *
def low(): 
    entry.delete(0, END) 
    length = var1.get() 
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""  
    if var.get() == 1: 
        for i in range(0, length): 
            password = password + random.choice(lower) 
        return password 
    elif var.get() == 0: 
        for i in range(0, length): 
            password = password + random.choice(upper) 
        return password 
    elif var.get() == 3: 
        for i in range(0, length): 
            password = password + random.choice(digits) 
        return password 
    else: 
        print("Please choose an option") 
def generate(): 
    password1 = low() 
    entry.insert(10, password1) 
def copy1(): 
    random_password = entry.get() 
    pyperclip.copy(random_password) 
root = Tk() 
var = IntVar() 
var1 = IntVar() 
root.title("Random Password Generator") 
Random_password = Label(root, text="Password") 
Random_password.grid(row=0) 
entry = Entry(root) 
entry.grid(row=0, column=1)  
c_label = Label(root, text="Length") 
c_label.grid(row=1) 
copy_button = Button(root, text="Copy", command=copy1) 
copy_button.grid(row=0, column=2) 
generate_button = Button(root, text="Generate", command=generate) 
generate_button.grid(row=0, column=3) 
radio_low = Radiobutton(root, text="Low", variable=var, value=1) 
radio_low.grid(row=1, column=2, sticky='E') 
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0) 
radio_middle.grid(row=1, column=3, sticky='E') 
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3) 
radio_strong.grid(row=1, column=4, sticky='E') 
combo = Combobox(root, textvariable=var1) 
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
                   17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, "Length") 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(column=1, row=1) 
root.mainloop()  






fn = open('bcd.txt', 'r')
fn1 = open('nfile.txt', 'w')
cont = fn.readlines() 
type(cont) 
for i in range(0, len(cont)): 
    if(i % 2 != 0): 
        fn1.write(cont[i]) 
    else: 
        pass
fn1.close()  
fn1 = open('nfile.txt', 'r')
print(cont1) 
fn.close() 
fn1.close() 

fn = open('bcd.txt', 'r')
fn1 = open('nfile.txt', 'w')
cont = fn.readlines() 
type(cont) 
for i in range(0, len(cont)): 
    if(i % 2 == 0): 
        fn1.write(cont[i]) 
    else: 
        pass
fn1.close()  
fn1 = open('nfile.txt', 'r')
print(cont1) 
fn.close() 
fn1.close() 



from tkinter import *
root = Tk()
 
root.geometry('200x200+100+200')

Label(text="Label 1", width=10).grid(row=0, column=0)
Label(text="Label 2", width=10).grid(row=0, column=1)
Label(root, text="Label 3 : x=0, y=0", bg="#FFFF00", fg="black").place(x=0, y=0)
Label(root, text="Label 4 : x=50, y=40", bg="#3300CC", fg="white").place(x=50, y=40)
label1 = Label(root, text="Label 5", bg="#E74C3C", fg="white").pack(fill=X, padx=10)
label2 = Label(root, text="Label 5", bg="#2ECC71", fg="black").pack(fill=X, padx=10)
mainloop()

from tkinter import*

master=Tk()

frame=Frame(master, width=300, height=300, background="yellow")

frame.pack()

master.mainloop()




import tkinter as tk 
 
class App(tk.Tk): 
    def __init__(self): 
        super().__init__() 
        frame = tk.Frame(self, bg="green", 
                         height=100, width=100) 
        frame.bind("<Button-1>", self.print_event) 
        frame.bind("<Double-Button-1>", self.print_event) 
        frame.bind("<ButtonRelease-1>", self.print_event) 
        frame.bind("<B1-Motion>", self.print_event) 
        frame.bind("<Enter>", self.print_event) 
        frame.bind("<Leave>", self.print_event) 
        frame.pack(padx=50, pady=50) 
 
    def print_event(self, event): 
        position = "(x={}, y={})".format(event.x, event.y) 
        print(event.type, "event", position) 
 
if __name__ == "__main__": 
    app = App() 
    app.mainloop() 
    
    
    
from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Welcome to Regidtration Form")
window.geometry('400x400')
window.configure(background = "grey");
a = Label(window ,text = "Name").grid(row = 0,column = 0)
b = Label(window ,text = "Emai Id").grid(row = 1,column = 0)
c = Label(window ,text = "Password").grid(row = 2,column = 0)
a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
def clicked():
 res = "Welcome to " + txt.get()
 lbl.configure(text= res)
btn = ttk.Button(window ,text="Register").grid(row=4,column=0)
window.mainloop()



from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Registration Form")


Fullname=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
Password= StringVar()



def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   password=Password.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT, Password TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Email,Gender,country, Password) VALUES(?,?,?,?,?)',(name1,email,gender,country, password,))
   conn.commit()
   
   
             
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Password",width=20,font=("bold", 10))
label_3.place(x=85,y=330)

entry_3 = Entry(root,textvar=Password)
entry_3.place(x=240,y=330)

label_4 = Label(root, text="Gender",width=20,font=("bold", 10))
label_4.place(x=70,y=230)

Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_5 = Label(root, text="country",width=20,font=("bold", 10))
label_5.place(x=70,y=280)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=280)



Button(root, text='Register',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)

root.mainloop()

"""

from tkinter import *
from math import *
 
#Function enables button clicks
def btnClick(numbers):
   global operator
   operator=operator+str(numbers)
   text_input.set(operator)
 
#Function enables 'C' button to clear display
def btnClearDisplay():
   global operator
   operator=""
   text_input.set("")
 
#Function enables completion of calculations
def btnEqualsInput():
   global operator
   sumof=str(eval(operator))
   text_input.set(sumof)
   operator=""
 
#Function enables square root calculations
def btnSquareRoot():
   global operator
   sqrt=math.sqrt()
   text_input.set("")
   operator=""
 
 
cal = Tk()
cal.title("Calculator")
operator=""
text_input=StringVar()
 
#Decides size, colour, etc. of display and font
txtdisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_input,bd=30,
                insertwidth=4,bg="powder blue",justify='right').grid(columnspan=3)
 
#Clear Button
btnClear=Button(cal,padx=10,bd=8,fg="black",font=('arial',20,'bold'),
               text="C",bg="Honeydew3",command=btnClearDisplay).grid(row=0,column=3)
 
#Top line

btnSquareRoot=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text="√",bg="Honeydew3",command=lambda:btnClick("sqrt")) .grid(row=1,column=1)
 
btnPercentage=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text="%",bg="Honeydew3",command=lambda:btnClick("/100*")).grid(row=1,column=1)
 
btnDivision=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text="/",bg="Honeydew3",command=lambda:btnClick("/")).grid(row=1,column=3)
 
#2nd line
btn7=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
           text="7",command=lambda:btnClick(7)).grid(row=2,column=0)
 
btn8=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
           text="8",command=lambda:btnClick(8)).grid(row=2,column=1)
 
btn9=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
           text="9",command=lambda:btnClick(9)).grid(row=2,column=2)
 
btnMultiplication=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text="*",bg="Honeydew3",command=lambda:btnClick("*")).grid(row=2,column=3)
 
#3rd line
btn4=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
           text="4",command=lambda:btnClick(4)).grid(row=3,column=0)
 
btn5=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
           text="5",command=lambda:btnClick(5)).grid(row=3,column=1)
 
btn6=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
           text="6",command=lambda:btnClick(6)).grid(row=3,column=2)
 
btnSubtraction=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text="-",bg="Honeydew3",command=lambda:btnClick("-")).grid(row=3,column=3)
 
#4th line
btn1=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
           text="1",command=lambda:btnClick(1)).grid(row=4,column=0)
 
btn2=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
           text="2",command=lambda:btnClick(2)).grid(row=4,column=1)
 
btn3=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
           text="3",command=lambda:btnClick(3)).grid(row=4,column=2)
 
btnAddition=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text="+",bg="Honeydew3",command=lambda:btnClick("+")).grid(row=4,column=3)
 
#Bottom line

 
btn0=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
           text="0",command=lambda:btnClick(0)).grid(row=1,column=0)
 
#btnPlusMinus=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
#               text="+/-",bg="Honeydew3").grid(row=5,column=2)

 
btnEquals=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),
               text="=",bg="tomato",command=btnEqualsInput).grid(row=1,column=2)
 
 
#Causes calculator to stay open
cal.mainloop()




"""from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Registration Form")


Fullname=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()



def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   prog=var1.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Programming) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog,))
   conn.commit()
   
   
             
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=280)

label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var2= IntVar()
Checkbutton(root, text="java", variable=var1).place(x=235,y=330)

Checkbutton(root, text="python", variable=var2).place(x=290,y=330)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)

root.mainloop()"""

 


