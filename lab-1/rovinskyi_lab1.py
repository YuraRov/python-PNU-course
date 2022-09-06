from math import sqrt, exp
from random import randint

# Task 7
# For the given number n < 100, complete the phrase "Zalik zdalo..."
# with the sentences "n studentiv", "n studenty" or "n student",
# using the correct results

""" n = input("Enter the quantity of students: ")
phrase = "Zalik zdalo"

if n.isnumeric():
    if n[-1] in "234":
        if len(n) > 1 and n[-2] == "1":
            result = f"{phrase} {n} studentiv"
        else:
            result = f"{phrase} {n} studenty"
    elif n[-1] == "1":
        if len(n) > 1 and n[-2] != "1" or n == "1":
            result = f"{phrase} {n} student"
        else:
            result = f"{phrase} {n} studentiv"
    else:
        result = f"{phrase} {n} studentiv"

print(result) """

# Task 8
# Input: 2 non-negative real numbers a and b. b is not equal to 0.
# Output data: a real number - the result of calculating the formula.

""" a = float(input())
b = float(input())

x = sqrt(a * b) / (exp(a) * b) + (a * exp(2 * a / b))
print(x) """

# Task 9
# Without using the arithmetic progression sum formula, calculate 1+x+x^2+...+x^n.
# The program receives an integer n and a real number x as input.

""" n = int(input())
x = float(input())
result = 0

for i in range(n + 1):
    result += x**i

print(result) """

# Task 10
# Write a cycle which generates 10 random natural numbers

for i in range(10):
    print(randint(1,10))
