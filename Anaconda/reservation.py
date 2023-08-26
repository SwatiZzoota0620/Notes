from functools import partial  
from tkinter import *
screen1=Tk()
screen1.title("Login Form")
screen1.geometry('500x300')
screen1.configure(bg='#A3E4D7')
                  
                  
def main_account_screen():
    
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("300x250") # set the configuration of GUI window 
    main_screen.title("Account Login") # set the title of GUI window

# create a Form label 
Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
Label(text="").pack() 

# create Login Button 
Button(text="Login", height="2", width="30").pack() 
Label(text="").pack() 

# create a register button
 Button(text="Register", height="2", width="30").pack()
 
main_screen.mainloop() # start the GUI

main_account_screen() # call the main_account_screen() function

                  
labelframe1 = LabelFrame(screen1, text="Login Details",bg ="#A3E4D7", height=270, width=450)  
labelframe1.pack()


lbl = Label(screen1, text="Login Form",bg="#E0F2F1", font=("Arial Bold", 15)).place(x=200,y=50)         
lbl1 = Label(screen1, text="Username",bg="#E0F2F1", font=("Arial", 15)).place(x=75,y=95)        
v = StringVar()
uname= Entry(screen1, width=30, textvariable=v).place(x=190,y=100)

lbl2 = Label(screen1, text="Password",bg="#E0F2F1", font=("Arial", 15)).place(x=75,y=145)         
p=StringVar()
pwd = Entry(screen1, width=30, textvariable=p).place(x=190,y=150)

                       
def msg():
    if ((v.get())=="swati" and (p.get())=="123456"):
        messagebox.showinfo("Title", "Suceessfully Login")
        
    else:
        messagebox.showinfo("Title", "Try Again")
        
btn = Button(screen1, text ="Login", fg="black",font=("Arial Bold", 15),bg="#FFECB3",command = msg).place(x=200,y=200)
             
             
def signup():
    from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registration Form")
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
entry_1 = Entry(root)
entry_1.place(x=240,y=130)
label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)
entry_2 = Entry(root)
entry_2.place(x=240,y=180)
label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
label_4 = Label(root, text="Age:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)
entry_2 = Entry(root)
entry_2.place(x=240,y=280)
Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)
# it is use for display the registration form on the window
root.mainloop()

screen1.mainloop()