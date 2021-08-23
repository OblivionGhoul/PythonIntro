# 1
class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def getA(self):
        return self.a
    
    def getB(self):
        return self.b
    
    def getC(self):
        return self.c
    
    def getD(self):
        return self.d
    
    def getE(self):
        return self.e
    
    def getF(self):
        return self.f

    def isSolvable(self):
        return "(", self.getX(), ",", self.getY(), ")"
    
    def getX(self):
        result = ((self.e * self.d) - (self.b * self.f)) / ((self.a * self.d) - (self.b * self.c))
        return result
    
    def getY(self):
        result = ((self.a * self.f) - (self.e * self.c)) / ((self.a * self.d) - (self.b * self.c))
        return result

# 3
import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def distance(self, newX, newY):
        result = math.sqrt(math.pow((newX - self.x), 2) + math.pow((newY - self.y), 2))
        return result
    
    def isNearBy(self, newX, newY):
        if self.distance(newX, newY) < 5:
            return True
        else:
            return False
    
    def __str__(self):
        return "(", self.x, ",", self.y, ")"

# 4
from tkinter import *

root = Tk()
root.title("Circle Mover")

width = 600
height = 600
x = width // 2
y = height // 2

def newCircle(x, y, r, canvasName):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)

myCanvas = Canvas(root, width = width, height = height, bg = "white")
myCanvas.pack(pady=20)

myCircle = newCircle(x, y, 10, myCanvas)

def left(event):
    x = -5
    y = 0
    myCanvas.move(myCircle, x, y)

def right(event):
    x = 5
    y = 0
    myCanvas.move(myCircle, x, y)

def up(event):
    x = 0
    y = -5
    myCanvas.move(myCircle, x, y)

def down(event):
    x = 0
    y = 5
    myCanvas.move(myCircle, x, y)

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()

# 5
num1, num2, num3, num4, num5 = eval(input("Enter 5 Numbers: "))
nums = [num1, num2, num3, num4, num5]
nums.reverse()
print("The new reversed list:", nums)