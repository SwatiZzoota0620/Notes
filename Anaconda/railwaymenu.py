from tkinter import * 

  
screen = Tk()  
screen.geometry('720x650')  
screen.configure(bg='#A3E4D7')
  
def hello():  
    print("hello!")  
  
# create a toplevel menu  
menubar = Menu(screen, font = "Courier 20")

menubar.add_command(label="Reservation", command=hello)  
menubar.add_command(label="Payment", command=hello) 
menubar.add_command(label="Exit", command=screen.quit)  
  
# display the menu  
screen.config(menu=menubar)  
  
screen.mainloop() 

