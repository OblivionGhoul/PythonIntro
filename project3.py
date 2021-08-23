# 3.4
import math
side = eval(input("Enter the side: "))
a = (5 * math.pow(side, 2)) / (4 * math.tan(math.pi/5))
print("The area of the pentagon is", a)

# 3.6
code = eval(input("Enter an ASCII code: "))
print("The ASCII character for this code is", chr(code))

# 3.5
import math
n = eval(input("Enter the number of sides: "))
s = eval(input("Enter the side length: "))
a = (n * (math.pow(s, 2))) / (4 * (math.tan(math.pi/n)))
print("The area of this polygon is", a)

# 3.10
import turtle
turtle.write("\u03b1 \u03b2 \u03b3 \u03b4 \u03b5 \u03b6 \u03b7 \u03b8")
turtle.done()