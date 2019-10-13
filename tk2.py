from Tkinter import *

win = Tk()
butt = []
happ = ['hi','my','name','is','trex']
for x in xrange(len(happ)) :
    butt.append(Button(win,text=happ[x]))
    
for n in xrange(len(happ)) :
    butt[n].pack()
checkbutt = Checkbutton(win,font = "please answer")
win.mainloop()
