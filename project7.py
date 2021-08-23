# 7.1
class Rectangle:
    # Construct a rectangle object
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def main():
        # Create a rectangle with width 4 and height 40
        r1 = Rectangle(4, 40)
        print("The width of the rectangle is", r1.width)
        print("The height of the rectangle is", r1.height)
        print("The area of the rectangle is", r1.getArea())
        print("The perimeter of the rectangle is", r1.getPerimeter())

        # Create a rectangle with width 3.5 and height 35.9
        r1 = Rectangle(3.5, 35.9)
        print("The width of the rectangle is", r1.width)
        print("The height of the rectangle is", r1.height)
        print("The area of the rectangle is", r1.getArea())
        print("The perimeter of the rectangle is", r1.getPerimeter())

    main()

# 7.3
class Account:
    def __init__(self, id = 0, balance = 100.0, annualInterestRate = 0.0):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate
    
    def getId(self):
        return self.id
    
    def setId(self, newId):
        self.id = newId

    def getBalance(self):
        return self.balance
    
    def setBalance(self, newBalance):
        self.balance = newBalance
    
    def getAnnualInterestRate(self):
        return self.annualInterestRate
    
    def setAnnaulInterestRate(self, newRate):
        self.annualInterestRate = newRate

    def getMonthlyInterest(self):
        return self.balance * ((self.annualInterestRate / 100) / 12)
    
    def withdraw(self, amountWithdrew):
        return self.balance - amountWithdrew

    def deposit(self, amountDeposited):
        return self.balance + amountDeposited

# 7.2
class Stock:
    def __init__(self, symbol, name, previousClosing, currentPrice):
        self.symbol = symbol
        self.name = name
        self.previousClosing = previousClosing
        self.currentPrice = currentPrice

    def getName(self):
        return self.name
    
    def getSymbol(self):
        return self.symbol

    def setStockPreviousPrice(self, setAmount):
        self.previousClosing = setAmount
    
    def getStockPreviousPrice(self):
        return self.previousClosing

    def setStockCurrentPrice(self, setAmount):
        self.currentPrice = setAmount

    def getStockCurrentPrice(self):
        return self.currentPrice

    def getChangePercent(self):
        previousPrice = self.previousClosing
        currentPrice = self.currentPrice
        result = format((currentPrice - previousPrice) * 100 / previousPrice, "5.2f") + "%"
        return result
    
    def main():
        test = Stock("INTC", "Intel Corporation", 20.5, 20.25)
        test.getChangePercent()
    
    main()

# 7.6
import math

class QuadratEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getC(self):
        return self.c
    
    def isDiscriminant(self):
        if ((self.b * self.b) - (4 * self.a * self.c)) >= 0:
            return True
        else:
            return False

    def getRoot1(self):
        if (QuadratEquation.isDiscriminant()):
            result = ((-1 * self.b) + math.sqrt(math.pow(self.b, 2) - (4 * self.a * self.c))) / (2 * self.a)
            return result
        else:
            return 0
    
    def getRoot2(self):
        if (QuadratEquation.isDiscriminant()):
            result = ((-1 * self.b) - math.sqrt(math.pow(self.b, 2) - (4 * self.a * self.c))) / (2 * self.a)
            return result
        else:
            return 0
    
    def main():
        a, b, c = eval(input("Enter the a, b, c values: "))
        test = QuadratEquation(a, b, c)
        if (test.getRoot1() or test.getRoot2()) == 0:
            print("The first root is", test.getRoot1())
        elif (test.getRoot1() and test.getRoot2()) != 0:
            print("Both roots are", test.getRoot1, "and", test.getRoot2)
        else:
            print("The equation has no roots.")
    
    main()

# 7.10
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def getHour(self):
        return self.hour

    def getMinute(self):
        return self.minute

    def getSecond(self):
        return self.second

    def setTime(self, time):
        self.second = time % 60
        totalMinutes = time // 60
        self.minute = totalMinutes % 60
        totalHours = totalMinutes // 60
        self.hour = totalHours % 24
    
    def main():
        test = Time(10, 10, 10)
        print("Current Time: ", test.getHour(), test.getMinute(), test.getSecond())
        time = eval(input("Enter the new time: "))
        test.setTime(time)
        print("New Time: ", test.getHour(), test.getMinute(), test.getSecond())
    
    main()