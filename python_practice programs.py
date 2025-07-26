 Basic Input/Output & Variables
Hello World


print("Hello, World!")
Calculator


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)

Temperature Converter


celsius = float(input("Enter temp in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)

Age Calculator


from datetime import date
birth_year = int(input("Enter birth year: "))
current_year = date.today().year
print("Your age is", current_year - birth_year)

Simple Interest Calculator


p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))
si = (p * r * t) / 100
print("Simple Interest:", si)

Area Calculator


shape = input("Choose shape (circle/rectangle/triangle): ").lower()
if shape == "circle":
    r = float(input("Radius: "))
    print("Area:", 3.1415 * r * r)
elif shape == "rectangle":
    l = float(input("Length: "))
    w = float(input("Width: "))
    print("Area:", l * w)
elif shape == "triangle":
    b = float(input("Base: "))
    h = float(input("Height: "))
    print("Area:", 0.5 * b * h)
    
Grade Calculator


percentage = float(input("Enter percentage: "))
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'
print("Grade:", grade)

Tip Calculator


bill = float(input("Enter bill amount: "))
tip = float(input("Enter tip percentage: "))
total = bill + (bill * tip / 100)
print("Total amount:", total)

🔁 Conditionals & Loops
Even/Odd Checker


n = int(input("Enter a number: "))
print("Even" if n % 2 == 0 else "Odd")

Leap Year Checker


year = int(input("Enter year: "))
print("Leap Year" if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else "Not Leap Year")

Number Guessing Game


import random
target = random.randint(1, 100)
guess = int(input("Guess a number (1-100): "))
while guess != target:
    guess = int(input("Try again: "))
print("Correct!")

Multiplication Table


num = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
    
Prime Number Checker


n = int(input("Enter number: "))
is_prime = all(n % i != 0 for i in range(2, int(n**0.5) + 1)) and n > 1
print("Prime" if is_prime else "Not Prime")

Factorial Calculator


n = int(input("Enter number: "))
fact = 1
for i in range(2, n+1):
    fact *= i
print("Factorial:", fact)

Sum of Digits


n = input("Enter a number: ")
print("Sum of digits:", sum(int(d) for d in n))

Pattern Printing

rows = 5
for i in range(1, rows+1):
    print('*' * i)

    
🔤 String Operations
Palindrome Checker


s = input("Enter string: ")
print("Palindrome" if s == s[::-1] else "Not Palindrome")

String Reverser


print(input("Enter string: ")[::-1])

Character Counter


s = input("Enter string: ")
ch = input("Character to count: ")
print("Count:", s.count(ch))

Word Counter


s = input("Enter sentence: ")
print("Word count:", len(s.split()))

String Validator (Password Strength)


import re
pw = input("Enter password: ")
if (len(pw) >= 8 and re.search(r'[A-Z]', pw) and 
    re.search(r'[a-z]', pw) and re.search(r'\d', pw)):
    print("Strong password")
else:
    print("Weak password")
    
Case Converter


s = input("Enter string: ")
print("Upper:", s.upper())
print("Lower:", s.lower())


Anagram Checker


a = input("First string: ")
b = input("Second string: ")
print("Anagram" if sorted(a) == sorted(b) else "Not Anagram")


📋 List Operations
List Manipulator


lst = [1, 2, 3]
lst.append(4)
lst.remove(2)
print("List contains 3:", 3 in lst)
print(lst)

List Sorter

lst = [5, 2, 9, 1]
print("Ascending:", sorted(lst))
print("Descending:", sorted(lst, reverse=True))

Duplicate Remover


lst = [1, 2, 2, 3, 4, 4]
print("Without duplicates:", list(set(lst)))

List Statistics

lst = [10, 20, 30]
print("Min:", min(lst), "Max:", max(lst), "Avg:", sum(lst)/len(lst))

List Merger

a = [1, 3, 5]
b = [2, 4, 6]
print("Merged & sorted:", sorted(a + b))

Matrix Operations (Addition & Multiplication)

# 2x2 Matrix Addition
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
add = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
print("Addition:", add)

# Matrix Multiplication
mul = [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
print("Multiplication:", mul)













