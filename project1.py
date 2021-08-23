# Q1.9
print("Area =", (4.5 * 7.9))
print("Perimeter =", (4.5 * 2) + (7.9 * 2))

# Q1.15
import turtle

turtle.right(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(50)
turtle.left(120)
turtle.forward(50)

turtle.done()

# Q1.3
print("FFFFFFF   U     U  NN     NN")
print("FF        U     U  NNN    NN")
print("FFFFFFF   U     U  NN N   NN")  
print("FF         U   U   NN  N  NN")
print("FF          UUU    NN    NNN")

# Q1.10
miles = 14/1.6
hours = 45.5/60
averageSpeed = miles/hours
print("The average speed is", averageSpeed,"miles per hour")

# Q1.11
currentPopulation = 312032486
time = 60 * 60 * 24 * 365 
born = time // 7 
death = time // 13
immigrant = time // 45

population = born + immigrant - death

for i in range(1, 6):
    currentPopulation += population
    print("The population is", currentPopulation, "in year", i)