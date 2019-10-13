from tkinter import *
from CGPA import *
def donothing():
     pass;

root = Tk()
root.title("CGPA CALCULATOR")
topframe = Frame(root)
topframe.pack()
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)

x = [frame1, frame2, frame3]
for i in x:
     i.pack()
     
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
# Menu Bar
menubar = Menu(root) 
filemenu = Menu(menubar, tearoff=0) 
filemenu.add_command(label="New", command=donothing) 
filemenu.add_command(label="Open", command=donothing) 
filemenu.add_command(label="Save", command=donothing) 
filemenu.add_command(label="Save as...", command=donothing) 
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()  
filemenu.add_command(label="Exit", command=root.quit) 
menubar.add_cascade(label="File", menu=filemenu) 
editmenu = Menu(menubar, tearoff=0) 
editmenu.add_command(label="Undo", command=donothing)  
  
editmenu.add_separator()  
editmenu.add_command(label="Cut", command=donothing) 
editmenu.add_command(label="Copy", command=donothing) 
editmenu.add_command(label="Paste", command=donothing) 
editmenu.add_command(label="Delete", command=donothing) 
editmenu.add_command(label="Select All", command=donothing)  
menubar.add_cascade(label="Edit", menu=editmenu) 
helpmenu = Menu(menubar, tearoff=0) 
helpmenu.add_command(label="Help Index", command=donothing) 
helpmenu.add_command(label="About...", command=donothing) 
menubar.add_cascade(label="Help", menu=helpmenu)  
root.config(menu=menubar)

name_label = Label(frame1, text="Full Name: ")
name_label.grid(row = 0)

name = Entry(frame1, bd=1)
name.grid(row = 0, column = 1)

matno_label = Label(frame1, text="Matriculation No: ")
matno_label.grid( row=1)

matno = Entry(frame1, bd=1)
matno.grid(row=1, column= 2)

dept_label = Label(frame1, text="Department: ")
dept_label.grid(row = 2)

dept = Entry(frame1, bd=1)
dept.grid(row = 2, column =2)

root.mainloop()
