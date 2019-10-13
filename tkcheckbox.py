from Tkinter import *
def checkB():
	pass
	return
	
window = Tk()
butt = Button(window, text="Display check-box", bg = "red", command = checkB )

chec = IntVar()
check1 = Checkbutton(window, text = "Haappy New year", variable = chec, \
		offvalue = 0, onvalue = 1, width = 50, height=50, state = ACTIVE )
butt.pack();check1.pack()
window.mainloop()
