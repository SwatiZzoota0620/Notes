import sqlite3
from tkinter import *

# create database or connect with existing database
conn = sqlite3.connect('student.db')
# create cursor
c = conn.cursor()

#create table
c.execute('''
Create table student(
name text,
gen text,
class text,
f_quiz_marks real,
s_quiz_marks  real,
t_quiz_marks real,
fr_quiz_marks real
)''')


# commit changes
conn.commit()
# close connection
conn.close()

# Starting with tkinter
root = Tk()
root.title('Database')


# Functions
def submit():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute('insert into student Values(:name, :gen, :class, :f_quiz_marks, :s_quiz_marks, :t_quiz_marks, :fr_quiz_marks)',
              {
                  'name': name.get(),
                  'gen': gen.get(),
                  'class': course.get(),
                  'f_quiz_marks': f_quiz_marks.get(),
                  's_quiz_marks': s_quiz_marks.get(),
                  't_quiz_marks': t_quiz_marks.get(),
                  'fr_quiz_marks': fr_quiz_marks.get()
              }
              )
    # Erase all the previous data
    name.delete(0, END)
    gen.delete(0, END)
    course.delete(0, END)
    f_quiz_marks.delete(0, END)
    s_quiz_marks.delete(0, END)
    t_quiz_marks.delete(0, END)
    fr_quiz_marks.delete(0, END)

    conn.commit()
    conn.close()


def query():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute('Select oid, * from student')
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + '\n'

    query_label = Label(frame, text=print_records)
    query_label.grid(row=13, column=0, columnspan=2)
    conn.commit()
    conn.close()


def first_query():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("Select class, AVG(f_quiz_marks + s_quiz_marks + t_quiz_marks + fr_quiz_marks) from student group by class")
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + '\n'

    query_label = Label(frame, text=print_records)
    query_label.grid(row=13, column=0, columnspan=2)
    conn.commit()
    conn.close()


def second_query():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("Select class, MAX(f_quiz_marks + s_quiz_marks + t_quiz_marks + fr_quiz_marks), MIN(f_quiz_marks + s_quiz_marks + t_quiz_marks + fr_quiz_marks) from student group by class")
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + '\n'

    query_label = Label(frame, text=print_records)
    query_label.grid(row=13, column=0, columnspan=2)

    conn.commit()
    conn.close()

def third_query():

    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute(f'Select * from student where oid={id.get()}')
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + '\n'

    query_label = Label(frame, text=print_records)
    query_label.grid(row=13, column=0, columnspan=2)

    # f = open("Exyz.txt", "a")
    # f.write(print_records)
    # f.close()
    conn.commit()
    conn.close()


# Frame
frame = LabelFrame(root, text='Frame', padx=10, pady=10)
frame.pack()

# Entry boxes
id = Entry(frame, width=30)
id.grid(row=0, column=1, pady=5, padx=20)
name = Entry(frame, width=30)
name.grid(row=1, column=1, pady=5, padx=20)
gen = Entry(frame, width=30)
gen.grid(row=2, column=1, pady=5, padx  =20)
course = Entry(frame, width=30)
course.grid(row=3, column=1, pady=5, padx=20)
f_quiz_marks = Entry(frame, width=30)
f_quiz_marks.grid(row=4, column=1, pady=5, padx=20)
s_quiz_marks = Entry(frame, width=30)
s_quiz_marks.grid(row=5, column=1, pady=5, padx=20)
t_quiz_marks = Entry(frame, width=30)
t_quiz_marks.grid(row=6, column=1, pady=5, padx=20)
fr_quiz_marks = Entry(frame, width=30)
fr_quiz_marks.grid(row=7, column=1, pady=5, padx=20)

# Labels
id_label = Label(frame, text='Student ID', padx=5, pady=5)
id_label.grid(row=0)
name_label = Label(frame, text='Name', padx=5, pady=5)
name_label.grid(row=1)
gen_label = Label(frame, text='Gender', padx=5, pady=5)
gen_label.grid(row=2)
course_label = Label(frame, text='Department', padx=5, pady=5)
course_label.grid(row=3)
f_quiz_marks_label = Label(frame, text='First Quiz Marks', padx=5, pady=5)
f_quiz_marks_label.grid(row=4)
s_quiz_marks_label = Label(frame, text='Second Quiz Marks', padx=5, pady=5)
s_quiz_marks_label.grid(row=5)
t_quiz_marks_label = Label(frame, text='Third Quiz Marks', padx=5, pady=5)
t_quiz_marks_label.grid(row=6)
fr_quiz_marks_label = Label(frame, text='Forth Quiz Marks', padx=5, pady=5)
fr_quiz_marks_label.grid(row=7)

# Buttons
submit_btn = Button(frame, text='ADD Student', bg='gray', fg='white', command=submit)
submit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

view_btn = Button(frame, text='VIEW ALL', bg='gray', fg='white', command=query)
view_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

view_1_btn = Button(frame, text='DISPLAY AVG', bg='gray', fg='white', command=first_query)
view_1_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

view_2_btn = Button(frame, text='HIGHEST & LOWEST ', bg='gray', fg='white', command=second_query)
view_2_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

view_3_btn = Button(frame, text='SEARCH BY ID', bg='gray', fg='white', command=third_query)
view_3_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# main loop
root.mainloop()

