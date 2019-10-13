import Tkinter
import tkMessageBox

def alerter():
		tkMessageBox.showinfo("Alert!!!","Your First Message Box is being created")
 
main_window = Tkinter.Tk()
button1 = Tkinter.Button(main_window,text="Happy", command = alerter)
canvas1 = Tkinter.Canvas(main_window,bg = "blue", height = 200,width= 200 )
arc = canvas1.create_arc((10,10,190,190),start = 0,extent = 359,fill = "red")		
button1.pack()
canvas1.pack()

main_window.mainloop()

