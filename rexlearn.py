from Tkinter import *

wind = Tk()

frm = Frame(wind)

lab = Label(frm, text="This is my First try \n\nSo please dont jugde me.",
            justify = LEFT)
ent = Entry(frm)
ent.pack(side = RIGHT)
lab.pack(side = LEFT)
frm.pack()

wind.mainloop()
