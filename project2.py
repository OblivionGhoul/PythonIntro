# 2.4
pounds = eval(input("Enter a number in pounds: "))
kilograms = pounds * 0.454
print(pounds, "pounds is", kilograms, "kilograms")

# 2.13
result = 0
number = eval(input("Enter an integer: "))
while(number > 0):
    num = number % 10
    result = result * 10 + num
    number = number // 10
 
print(result)

# 2.1
celsius = eval(input("Enter a degree in Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(celsius, "Celsius is", fahrenheit, "Fahrenheit")

# 2.2
radius = eval(input("Enter the radius of the circle: "))
length = eval(input("Enter the length of the circle: "))
area = 3.14 * radius * radius
volume = area * length
print("The area of the circle is", area, "and the volume is", volume)

# 2.10
v, a = eval(input("Enter the speed and acceleration: "))
length = (v * v) / (2 * a)
print("Minimum runway length needed:", length)