from tkinter import *

#wind1 = Tk()
#wind1.mainloop()

store = 0

def add():
    x = int(input("Enter :"))
    global store
    store = store + x
    return store

def show():
    global store
    print (store)
    

eval(input("Enter Operation: "))

