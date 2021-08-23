# 1
balance = eval(input("Enter the current balance: "))
annualPercentage = eval(input("Enter the annual percent interest rate: "))
interest = balance * (annualPercentage * 0.01) * 1/12
print("Next month's interest:", interest)

# 2
import math
import turtle
x1, y1 = eval(input("Enter the first point: "))
x2, y2 = eval(input("Enter the second point: "))
x3, y3 = eval(input("Enter the third point: "))

side1 = math.pow(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2), 0.5)
side2 = math.pow(math.pow(x3 - x2, 2) + math.pow(y3 - y2, 2), 0.5)
side3 = math.pow(math.pow(x1 - x3, 2) + math.pow(y1 - y3, 2), 0.5)
s = (side1 + side2 + side3) / 2
area = math.pow(s * (s - side1) * (s - side2) * (s - side3), 0.5)
print("The area of the triangle is", area)

turtle.pendown()
turtle.done()

# 3
x, y = eval(input("Enter the points: "))
if (((x > -2.5 and x < 2.5) and (y > -5 and y < 5)) | ((x > -5 and x < 5) and (y > -2.5 and y < 2.5))):
    print("The points are in the rectangle.")
else:
    print("The points are not in the rectangle.")

# 4
num = 1000
def isPrime(n):
    for i in range(2, n):
         if n % i == 0:
            return False
    return True

for i in range(2, num):
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        if isPrime(i+2):
            print("(", i, ",", i+2, ")")