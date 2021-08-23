# 4.9
weight1, price1 = eval(input("Enter weight and price for package 1: "))
weight2, price2 = eval(input("Enter weight and price for package 2: "))

p1 = price1/weight1
p2 = price2/weight2

if p1 > p2:
    print("The second price is better.")
elif p1 < p2:
    print("The first price is better.")
else:
    print("They are the same price.")

# 4.19
edge1, edge2, edge3 = eval(input("Enter three edges (length in double): "))
isTriangle = ((edge1 + edge2 > edge3) | (edge1 + edge3 > edge2)
              | (edge3 + edge2 > edge1))

if isTriangle:
    print("The perimeter is", edge1 + edge2 + edge3)
else:
    print("This is not a valid triangle!")

# 4.8
num1, num2, num3 = eval(input("Enter 3 ints: "))
if (num1 > num2 & num1 > num3 & num2 > num3): 
    print(num3, num2, num1)
elif (num2 > num1 & num3 > num2):
    print(num1, num2, num3)
elif (num2 < num1 & num2 < num3 & num1 > num3):
    print(num2, num3, num1)
elif (num2 < num1 & num2 < num3 & num3 > num1):
    print(num3, num1, num2)
elif (num2 < num1 & num2 < num3 & num3 < num1):
    print(num1, num3, num2)
else:
    print(num2, num1, num3)

# 4.10
import random
num1 = random.randint(0, 99)
num2 = random.randint(0, 99)

answer = eval(input("What is " + str(num1) + " * " + str(num2) + "? "))
if answer == num1 * num2:
    print("You are correct!")
else: 
    print("You are incorrect, the answer:", num1 * num2)

# 4.13
import sys

status = eval(input("(0-single filer, 1-married jointly,\n" +
              "2-married separately, 3-head of household)\n" + "Enter the filing status: "))

income = eval(input("Enter the taxable income: "))

tax = 0
if status == 0:
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (income - 33950) * 0.25
    elif income <= 171550:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (82250 - 33950) * 0.25 + (income - 82250) * 0.28
    elif income <= 372950:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
            (income - 171550) * 0.33
    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
            (372950 - 171550) * 0.33 + (income - 372950) * 0.35
elif status == 1:
    if income <= 16700:
        tax = income * 0.10
    elif income <= 67900:
        tax = 16700 * 0.10 + (income - 16700) * 0.15
    elif income <= 137050:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
            (income - 67900) * 0.25
    elif income <= 208850:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
            (137050 - 6700) * 0.25 + (income - 137050) * 0.28
    elif income <= 372950:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
            (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + \
            (income - 208850) * 0.33
    else:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
            (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + \
            (372950 - 208850) * 0.33 + (income - 372950) * 0.35
elif status == 2:
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 68525:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (income - 33950) * 0.25
    elif income <= 104425:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (68525 - 33950) * 0.25 + (income - 68525) * 0.28
    elif income <= 186475:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
            (income - 104425) * 0.33
    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
            (186475 - 104425) * 0.33 + (income - 186475) * 0.35

elif status == 3:
    if income <= 11950:
        tax = income * 0.10
    elif income <= 45500:
        tax = 11950 * 0.10 + (income - 11950) * 0.15
    elif income <= 117450:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
            (income - 45500) * 0.25
    elif income <= 190200:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
            (117450 - 45500) * 0.25 + (income - 117450) * 0.28
    elif income <= 372950:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
            (117450 - 45500) * 0.25 + (104425 - 117450) * 0.28 + \
            (income - 192200) * 0.33
    else:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
            (117450 - 45500) * 0.25 + (192200 - 117450) * 0.28 + \
            (186475 - 192200) * 0.33 + (income - 372950) * 0.35
else:
    print("Error: invalid status")
    sys.exit()

print("Tax is", int(tax * 100) / 100.0)