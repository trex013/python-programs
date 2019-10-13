import tkinter
def open_file():
    "this creates a new file"
    file1 = open("file1.txt","a")
    file1.write("happy")
    file1.close
    return

window = tkinter.Tk()
button = tkinter.Button(window, text = "One Love", command = open_file)
canvas = tkinter.Canvas(window, height=200, width=250)
coord = 5,5,150,150
arc = canvas.create_arc(coord,start = 30,extent = 300 ,fill = "black")
canvas.pack()

button.pack()

window.mainloop()
