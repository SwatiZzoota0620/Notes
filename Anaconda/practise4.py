import tkinter as tk  
from functools import partial  
from tkcalendar import Calendar,DateEntry
     
screen2 = tk.Tk()  
screen2.geometry('720x650')  
  
screen2.title('Railway Reservation Form') 
screen2.configure(bg='#B3E5FC')


labelframe1 = LabelFrame(screen2, text="Booking Details",font=("calibri Bold", 15),bg="#B3E5FC", fg="#424242" ,  height=270, width=690).place(x=8,y=25)  
  
lbl1 = Label(screen2, text="From",bg="#E1F5FE", font=("calibri")).place(x=10,y=55)       
v1 = StringVar()
entry1= Entry(screen2, textvariable=v1).place(x=170,y=60)
lbl2 = Label(screen2, text="To",bg="#E1F5FE", font=("calibri")).place(x=350,y=55)       
v2 = StringVar()
entry2= Entry(screen2, textvariable=v2).place(x=500,y=60)
 
    
lbl3 = Label(screen2, text="Preferred Airline",bg="#E1F5FE", font=("calibri")).place(x=10,y=115)       
v3 = StringVar()
entry3= Entry(screen2, textvariable=v3).place(x=170,y=120)
lbl4 = Label(screen2, text="Prefered Seating",bg="#E1F5FE", font=("calibri")).place(x=350,y=115)       
v4 = StringVar()
entry4= Entry(screen2, textvariable=v4).place(x=500,y=120)

lbl5 = Label(screen2, text="Departure Date",bg="#E1F5FE", font=("calibri")).place(x=10,y=175)       
v5 = StringVar()
cal = DateEntry(screen2,year=2019,  textvariable=v5).place(x=170,y=180)
lbl6 = Label(screen2, text="Departure time",bg="#E1F5FE", font=("calibri")).place(x=350,y=175)       
v6 = StringVar()
entry5= Entry(screen2, textvariable=v6).place(x=500,y=180)



lbl7 = Label(screen2, text="Age(12+ Yrs)",bg="#E1F5FE", font=("calibri")).place(x=10,y=235)       
v7 = StringVar()
entry6= Spinbox(screen2, from_= 12, to = 110, width=5,  textvariable=v7).place(x=140,y=240)
lbl8 = Label(screen2, text="Children(2-11 Yrs)",bg="#E1F5FE", font=("calibri")).place(x=200,y=235)       
v8= StringVar()
entry7= Spinbox(screen2, from_= 2, to = 11, width=5,  textvariable=v8).place(x=370,y=240) 
lbl8 = Label(screen2, text="Infant(under 2 Yrs)",bg="#E1F5FE", font=("calibri")).place(x=430,y=235)       
v9 = StringVar()
entry8= Spinbox(screen2, from_= 1, to = 1, width=5,  textvariable=v9).place(x=600,y=240)  


lbl9 = Label(screen2, text="Select Your Fare",bg="#B3E5FC", font=("calibri Bold", 15)).place(x=65,y=305)
R1 = Radiobutton(screen2, text="One Way",bg="#B3E5FC", value=1, font=("calibri")).place(x=220,y=300)    
R2 = Radiobutton(screen2, text="Round Trip",bg="#B3E5FC", value=2, font=("calibri")).place(x=380,y=300) 

lbl10 = Label(screen2, text="Return Date",bg="#B3E5FC", font=("calibri")).place(x=105,y=345)       
v8 = StringVar()
cal = DateEntry(screen2,year=2019).place(x=230,y=350)
lbl11 = Label(screen2, text="Return time",bg="#B3E5FC", font=("calibri")).place(x=340,y=345)       
v9 = StringVar()
entry9= Entry(screen2, textvariable=v2).place(x=465,y=350)   


labelframe2 = LabelFrame(screen2, text="Personal Details",font=("calibri Bold", 15), bg="#B3E5FC", fg="#424242", height=130, width=690).place(x=8,y=400)
  
lbl12 = Label(screen2, text="Full Name",bg="#E1F5FE", font=("calibri")).place(x=10,y=435)       
v1 = StringVar()
entry10= Entry(screen2, textvariable=v1).place(x=170,y=440)
lbl13 = Label(screen2, text="Phone Number",bg="#E1F5FE", font=("calibri")).place(x=350,y=435)       
v2 = StringVar()
entry11= Entry(screen2, textvariable=v2).place(x=500,y=440)
lbl14 = Label(screen2, text="Email",bg="#E1F5FE", font=("calibri")).place(x=10,y=490)       
v2 = StringVar()
entry12= Entry(screen2, textvariable=v2).place(x=170,y=495)

btn = Button(screen2, text ="Submit", fg="black",font=("Arial Bold", 15), bg="#FFCCBC",command = msg).place(x=190,y=570)
btn = Button(screen2, text ="Clear Form", fg="black",font=("Arial Bold", 15), bg="#FFCCBC",command = msg).place(x=340,y=570)
    
screen2.mainloop()  