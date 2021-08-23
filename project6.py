# 6.9
def footToMeter(foot):
    meter = 0.305 * foot
    return meter

def meterToFoot(meter):
    foot = meter / 0.305
    return foot

# 6.18
import random
def main():
    printMatrix(3)
    
def printMatrix(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(random.randint(0, 1), end = " ")

        print()    
main()

# 6.6
def main():
    lineNumber = eval(input("Enter line number: "))
    displayPattern(lineNumber)
    
def displayPattern(n):
    for row in range(1, n + 1):
        for j in range(n, row - 1, -1):
            print(format(" ", "2s"), end=" ")
        for j in range(row, 0, -1):
            print(format(j, "2d"), end=" ")
        print()
main()
'''
# 6.10
num = 0
for i in range(1, 10001):
    if isPrime(i):
        num += 1
print("The number of prime numbers less than 10,000:", num)

# 6.39
import turtle
import math
from UsefulTurtleFunctions import drawLine
drawLine(x1, y1, x3, y3)
drawLine(x1, y1, x4, y4)
drawLine(x2, y2, x4, y4)
drawLine(x2, y2, x5, y5)
drawLine(x3, y3, x5, y5)
turtle.hideturtle()
turtle.done()
'''