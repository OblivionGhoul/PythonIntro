# 9.3
from tkinter import *

class GUI:
    def __init__(self):
        window = Tk()
        self.v1 = IntVar()
        self.v2 = IntVar()
        self.c = Canvas(window, width=200, height=200, bg="white")
        self.c.pack()
        f = Frame(window)
        rrb = Radiobutton(f, text="Rectangle", variable=self.v1, value=1, command=self.draw).grid(row=1, column=1)
        orb = Radiobutton(f, text="Oval", variable=self.v1, value=2, command=self.draw).grid(row=1, column=2)
        fillcb = Checkbutton(f, text="Filled", variable=self.v2).grid(row=1, column=3)
        f.pack()

        window.mainloop()

    def draw(self):
        self.c.delete("r","o")
        if self.v2.get() == 1:
            if self.v1.get() == 1:
                self.c.create_rectangle(10, 10, 200, 100, fill="gray", tag="r")
            else:
                self.c.create_oval(10, 10, 200, 100, fill="gray", tag="o")
        else:
            if self.v1.get() == 1:
                self.c.create_rectangle(10, 10, 200, 100,tag="r")
            else:
                self.c.create_oval(10, 10, 200, 100,tag="o")

GUI()

# 9.4
from tkinter import *

window = Tk()
c = Canvas(window,width=300,height=200,bg="white")
c.pack()
x1 = 3; y1 = 3; x2=299; y2=199

for i in range(20):
    c.create_rectangle(x1+5,y1+5,x2-5,y2-5)
    x1 = x1+5; y1 = y1+5; x2 = x2-5; y2 = y2-5
window.mainloop()

# 9.6
import random
from tkinter import *

window = Tk()
x = PhotoImage(file="x.gif")
o = PhotoImage(file="o.gif")
for i in range(3):
    for j in range(3):
        r = random.randint(0, 1)
        if r == 0:
            Label(window, image=x).grid(row=i + 1, column=j + 1)
        elif r == 1:
            Label(window, image=o).grid(row=i + 1, column=j + 1)

window.mainloop()

# 9.10
from tkinter import * 
import math

radius = 50
width = 250
height = 250

class GUI:
    def drawAPie(self, start, extent, color, title):
        self.canvas.create_arc(width / 2 - radius, height / 2 - radius,
                               width / 2 + radius, height / 2 + radius,
                               start=start, extent=extent, fill=color)
        x = width / 2 + radius * math.cos(math.radians(extent / 2 + start))
        y = height / 2 - radius * math.sin(math.radians(extent / 2 + start))
        self.canvas.create_text(x, y, text=title)

    def __init__(self):
        window = Tk() 
        window.title("Pie Chart") 

        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()

        self.drawAPie(0, 360 * 0.2, "red", "Project -- 20%")
        self.drawAPie(360 * 0.2, 360 * 0.1, "blue", "Quizzes -- 10%")
        self.drawAPie(360 * 0.2 + 360 * 0.1, 360 * 0.3, "green", "Midterm -- 30%")
        self.drawAPie(360 * 0.2 + 360 * 0.1 + 360 * 0.3, 360 * 0.4, "orange", "Final -- 40%")

        window.mainloop()

GUI()

# 9.18
from tkinter import *

width = 300
height = 200

class GUI:
    def __init__(self):
        window = Tk() 
        window.title("Flashing Text")

        sleepTime = 100
        canvas = Canvas(window, bg="white", width=width, height=height)
        canvas.pack()

        on = True
        while True:
            if on:
                canvas.create_text(width / 2, height / 2, text="Welcome.", tags="text")
            else:
                canvas.delete("text")

            on = not on
            canvas.after(sleepTime)
            canvas.update()

        window.mainloop()

GUI()