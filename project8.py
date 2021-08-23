# 8.3
def main():
    s = input("Enter a string for password: ").strip()
    if isValidPassword(s):
        print("Valid password")
    else:
        print("Invalid password")

# Check if a string is a valid password 
def isValidPassword(s):
    # Only letters and digits?
    if not s.isalnum():
        return False
        
    # Check length
    if len(s) < 8:
        return False
        
    # Count the number of digits
    count = 0
    for ch in s:
        if ch.isdigit(): 
            count += 1
            
    if count >= 2:
        return True
    else:
        return False
    
main()

# 8.11
def main():
    string = input("Enter a word to reverse: ").strip()
    print(reverse(string))

def reverse(s):
    string = s[len(s):0:-1] + s[0]
    return string

main()

# 8.2
def main():
    first = input("Enter the first string: ").strip()
    second = input("Enter the second string: ").strip()
    
    if isSubstring(first, second) != -1: 
        print(first, "is a substring of", second)
    else:
        print(first, "is not a substring of", second)

def isSubstring(first, second):
    return second.find(first)

main()

# 8.7
def main():
    s = input("Enter a string: ").strip().upper()
    
    for ch in s:
        if ch.isalpha():
            print(getNumber(ch), end = "")
        else:
            print(ch, end = "")

def getNumber(uppercaseLetter):
    number = 0
    if uppercaseLetter == 'A' or uppercaseLetter == 'B' or uppercaseLetter == 'C':
        number = 2
    elif uppercaseLetter == 'D' or uppercaseLetter == 'E' or uppercaseLetter == 'F':
        number = 3
    elif uppercaseLetter == 'G' or uppercaseLetter == 'H' or uppercaseLetter == 'I':
        number = 4
    elif uppercaseLetter == 'J' or uppercaseLetter == 'K' or uppercaseLetter == 'L':
        number = 5
    elif uppercaseLetter == 'M' or uppercaseLetter == 'N' or uppercaseLetter == 'O':
        number = 6
    elif uppercaseLetter == 'P' or uppercaseLetter == 'Q' or uppercaseLetter == 'R' or uppercaseLetter == 'S':
        number = 7
    elif uppercaseLetter == 'T' or uppercaseLetter == 'U' or uppercaseLetter == 'V':
        number = 8
    elif uppercaseLetter == 'W' or uppercaseLetter == 'X' or uppercaseLetter == 'Y' or uppercaseLetter == 'Z':
        number = 9
    
    return number

main()

# 8.10
def main():
    value = eval(input("Enter an integer: "))
    print("The binary value is", decimalToBinary(value))

def decimalToBinary(value):
    return format(value, "b")

main()