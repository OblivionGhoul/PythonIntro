# 10.1
def main():
    s = input("Enter scores separated by spaces from one line: ")
    items = s.split()
    scores = [ eval(x) for x in items ]
    best = max(scores)

    for x in range(len(scores)):
        if scores[x] >= best - 10:
            print("Student", x, "score is", scores[x], "and grade is A")
        elif scores[x] >= best - 20:
            print("Student", x, "score is", scores[x], "and grade is B")
        elif scores[x] >= best - 30:
            print("Student", x, "score is", scores[x], "and grade is C")
        elif scores[x] >= best - 40:
            print("Student", x, "score is", scores[x], "and grade is D")
        else:
            print("Student", x, "score is", scores[x], "and grade is F")

main()

# 10.8
def indexOfSmallestElement(lst):
    smallestElement = 0
    smallestNum = lst[0]

    for i in range(len(lst)):
        if lst[i] < smallestNum:
            smallestNum = lst[i]
            smallestElement = i
    
    return smallestElement

def main():
    s = input("Enter scores separated by spaces from one line: ")
    items = s.split() # Extracts items from the string
    numbers = [ eval(x) for x in items ] # Convert items to numbers
    print("The index of the smallest element is", indexOfSmallestElement(numbers))

main()

# 10.4
def main():
    s = input("Enter the numbers: ") 
    items = s.split() # Extracts items from the string
    scores = [ eval(x) for x in items ] # Convert items to numbers
    
    numOfAbove = 0
    average = sum(scores) / len(scores)

    for i in range(len(scores)):
        if scores[i] >= average:
            numOfAbove += 1
    
    print("Average is", average)
    print("Number of scores above or equal to the average", numOfAbove)
    print("Number of scores below the average", len(scores) - numOfAbove)

main()

# 10.13
def eliminateDuplicates(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)

    return result

def main():
    s = input("Enter the numbers: ")
    items = s.split()
    scores = [ eval(x) for x in items ]
    print(eliminateDuplicates(scores))

main()

# 10.26
def main():
    s = input("Enter list1: ") 
    items = s.split() # Extracts items fromthe string
    list1 = [ eval(x) for x in items ] # Convert items to numbers

    s = input("Enter list2: ") 
    items = s.split() # Extracts items from the string
    list2 = [ eval(x) for x in items ] # Convert items to numbers

    list3 = merge(list1, list2)

    print("The merged list is ", end = "")
    for e in list3:
        print(e, end = " ")

def merge(list1, list2):
    result = []
    c1 = 0
    c2 = 0
    while c1 < len(list1) and c2 < len(list2):
        m1 = list1[c1]
        m2 = list2[c2]
        if m1 < m2:
            result.append(m1)
            c1 += 1
        else:
            result.append(m2)
            c2 += 1

    while c1 < len(list1):
        result.append(list1[c1])
        c1 += 1

    while c2 < len(list2):
        result.append(list2[c2])
        c2 += 1

    return result

main()