# 5.18
number = eval(input("Enter a positive integer: "))
print("The factors for", number, "is", end = " ")

factor = 2
while factor <= number:
    if number % factor == 0:
        number = number / factor
        print(factor, end = ",")    
    else:
        factor += 1

# 5.26
sum = 0
for i in range(1, 97 + 1, 2):
    sum += i / (i + 2)

print("Sum is", sum)

# 5.2
import random
import time

correct = 0
count = 0
NUMBER_OF_QUESTIONS = 10
startTime = time.time()
while count < NUMBER_OF_QUESTIONS:
    n1 = random.randint(1, 15)
    n2 = random.randint(1, 15)
    ans = eval(input("What is " + str(n1) + " + " + str(n2) + " = "))

    if ans == (n1 + n2):
        print("You are correct!")
        correct += 1
    else:
        print("Your answer is wrong.\n", n1, "+", n2, "=", (n1 + n2))

    count += 1

endTime = time.time()
testTime = int(endTime - startTime)
print("Correct count is", correct, "out of", NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")

# 5.28
temp = 1
e = 1

for i in range(1, 100000 + 1):
    temp = temp / i
    e += temp

    if (i == 10000 or i == 20000 or i == 30000 or i == 40000 or i == 50000 or 
        i == 60000 or i == 70000 or i == 80000 or i == 90000 or i == 100000):
        print("The e is", e, "for i =", i)