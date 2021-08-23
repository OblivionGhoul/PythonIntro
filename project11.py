# 11.1
def main():
    matrix = []

    for i in range(3):
        s = input("Enter a 3 by 4 matrix row " + str(i) + ": ")
        items = s.split()
        list = [ eval(x) for x in items]
        matrix.append(list)
    
    for i in range(4):
        print("Sum of the elements for column " + str(i) + " is", sumColumn(matrix, i))

def sumColumn(m, columnIndex):
    sum = 0
    for i in range(len(m)):
        sum += m[i][columnIndex]

    return sum

main()

# 11.3
def main():
    answers = [
        ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
        ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
        ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
        ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]

    keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
    studentList = []

    for i in range(len(answers)):
        correctCount = 0
        for j in range(len(answers[i])):
            if answers[i][j] == keys[j]:
                correctCount += 1

        studentList.append([correctCount, "Student " + str(i)])

    studentList.sort()
    for row in studentList:
        print(row[1], "has", row[0], "correct answers")

main()

# 11.4
workHours = [
    [2, 4, 3, 4, 5, 8, 8],
    [7, 3, 4, 3, 3, 4, 4],
    [3, 3, 4, 3, 3, 2, 2],
    [9, 3, 4, 7, 3, 4, 1],
    [3, 5, 4, 3, 6, 3, 8],
    [3, 4, 4, 6, 3, 4, 4],
    [3, 7, 4, 8, 3, 8, 4],
    [6, 3, 5, 9, 2, 7, 9]]

matrix = []

for row in range(len(workHours)):
    totalHours = sum(workHours[row])
    matrix.append([totalHours, "Employee " + str(row)])

matrix.sort(reverse = True)

for i in matrix:
    print("Hours of", i[1]+":", i[0])

# 11.8
import math

def main():
    points = [[0, 0, 0], [9, 9, 9], [-1, 0, 3], 
          [-1, -1, -1], [4, 1, 1], [4, 1, 2], 
          [4, 1, 0], [2, 0.5, 9], [3.5, 2, -1], 
          [3, 1.5, 3], [-1.5, 4, 2],[5.5, 4, -0.5]]
    
    p1 = 0
    p2 = 1
    list1 = [[p1, p2]]
    shortestDistances = distance( #Initialize shortestDistancespoints
        [p1][0], points[p1][1], points[p1][2], # <x1, y1, z1> points
        [p2][0], points[p2][1], points[p2][2])
    
    for x in range(len(points)):
        d = distance(
            [p1][x], points[p1][x + 1], points[p1][x + 2],
            [p2][x], points[p2][x + 1], points[p2][x + 2])
        
        if shortestDistances > d:
            list1.clear()
            list1.append([x, x + 1, x + 2])
            shortestDistances = d
        elif shortestDistances == d:
            list1.append([x, x + 1, x + 2])
        
def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 -x1) * (x2 -x1) + (y2 -y1) * (y2 -y1) + \
        (z2 -z1) * (z2 -z1))
        
main()
# 11.13
def locateLargest(a):
    maxRow = 0
    maxCol = 0

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > a[maxRow][maxCol]:
                maxRow = i
                maxCol = j

    return maxRow, maxCol

def main():
    rows = int(input("Enter the number of rows in the list: "))
    matrix = []

    for i in range(rows):
        r = input("Enter row " + str(i + 1) + ": " ).split()
        r = [float(x) for x in r]
        matrix.append(r)

    row, col = locateLargest(matrix)
    print("The location of the largest element is at: (" + str(row) + "," + str(col) + ")")

main()