from tkinter import *
from datetime import datetime as dt
from threading import Thread as th
from random import choice
import time


class Timer :
     def time(self, countD):
          self.cursec = dt.today().second

          while True:
               #print(self.cursec,"Current sec:", dt.today().second)
               if self.cursec + countD == dt.today().second:
                    return True;

     def setTimeout(self, seconds, fn, *args):
          
          t = th(target=fn, args=(args))
          #self.time(seconds)
          time.sleep(seconds)
          t.start()
          del(t)
          #fn(*args)

     def setInterval(self, sec, fn, *args):
          t = th(target=fn, args=(args))
          time.sleep(sec)
          t.start()
          self.setInterval(sec,fn,*args)
          #self.setTimeout(self.sec,self.setInterval, self.fnc, args)
          

def Main():
     root = Tk()
     def draw2(x, x1,y1, x2,y2):
          x.delete(ALL)
          x1 = x1 + 2
          y1 = y1 + 2
          x2 = x2 + 2
          y2 = y2 + 2
          colors = ["red", "green","pink","yellow"]
          color = choice(colors)
          x.create_rectangle(x1,y1,x2,y2, fill= color)
          Timer().setTimeout(.1,draw2,x,x1,y1,x2,y2)

     

     canvas = Canvas(root, width=400, height=400)
     canvas.pack()
     box = canvas.create_rectangle(20,20,40,40, fill= "green")
     Timer().setTimeout(0,draw2,canvas,60,60,40,40)
     
     root.mainloop()

Main()
