# 1
def prefix(s1, s2):
    if len(s1) < len(s2):
        shorter = s1
    else:
        shorter = s2

    for i in range(1, len(shorter)+1):
        if not s1[:i] == s2[:i]:
            return s1[:i-1]
    return shorter

def main():
    str1 = input("Enter String 1: ")
    str2 = input("Enter String 2: ")
    print("Prefix:", prefix(str1, str2))

main()

# 2
from tkinter import *

wide = 200
high = 400

window=Tk()
window.title("Traffic Light")
        
frame=Frame(window)
frame.pack()

def newLight(self):
    self.color=StringVar()
    self.color.set("B")
        
    rdRed=Radiobutton(frame, text="Red", variable=self.color, value="R", command=self.processRadio)
    rdRed.grid(row=10, column=1)
        
    rdYellow=Radiobutton(frame, text="Yellow", variable=self.color, value="Y", command=self.processRadio)
    rdYellow.grid(row=10, column=2)
        
    rdGreen=Radiobutton(frame, text="Green", variable=self.color, value="G", command=self.procesRadio)
    rdGreen.grid(row=10, column=3)
        
    self.canvas=Canvas(window, width=wide, height=high)
    self.canvas.pack()
        
    self.oRed=self.canvas.create_oval(30,10,140,110)
    self.oYel=self.canvas.create_oval(30,110,140,210)
    self.oGr=self.canvas.create_oval(30,210,140,310)
    self.canvas.create_rectangle(30,10,140,310)
    
def processRadio(self):
    color=self.color.get()
    if color=="R":
        self.canvas.itemconfig(self.oRed, fill="red")
        self.canvas.itemconfig(self.oYel, fill="white")
        self.canvas.itemconfig(self.oGr, fill="white")
        
    elif color=="Y":
        self.canvas.itemconfig(self.oRed, fill="white")
        self.canvas.itemconfig(self.oYel, fill="yellow")
        self.canvas.itemconfig(self.oGr, fill="white")
        
    elif color=="G":
        self.canvas.itemconfig(self.oRed, fill="white")
        self.canvas.itemconfig(self.oYel, fill="white")
        self.canvas.itemconfig(self.oGr, fill="green")

window.mainloop()

# 3
def reverseSort(nums):
    if len(nums) <= 1:
        return nums
    else:
        largest = max(nums)
        nums.remove(largest)
        return reverseSort(nums) + [largest]

def main():
    nums = [5, 4, 7, 9, 3, 20]
    print(reverseSort(nums))

main()

# 4
import random
arr = [[random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
      [random.randint(0, 1), random.randint(0, 1),
                      random.randint(0, 1), random.randint(0, 1)],
      [random.randint(0, 1), random.randint(0, 1),
                      random.randint(0, 1), random.randint(0, 1)],
       [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]]

print('\n'.join([''.join([str(x) for x in row]) for row in arr]))

largest_rows = []
most_ones = 0
for i in range(4):
    if sum(arr[i]) > most_ones:
        most_ones = sum(arr[i])
        largest_rows = [i]
    elif sum(arr[i]) == most_ones:
        largest_rows.append(i)

largest_cols = []
most_ones = 0
for i in range(4):
    num_ones = 0
    for j in range(4):
        num_ones += arr[j][i]
    if num_ones > most_ones:
        most_ones = num_ones
        largest_cols = [i]
    elif num_ones == most_ones:
        largest_cols.append(i)

print(f"The largest row index: {', '.join([str(x) for x in largest_rows])}")
print(f"The largest col index: {', '.join([str(x) for x in largest_cols])}")