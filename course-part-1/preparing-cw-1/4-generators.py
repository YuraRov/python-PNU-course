# Скласти програми.docx
# This script contains the solution for task №7

from math import factorial
from typing import Iterator

# Generator expression
factorial_expression = (factorial(i) for i in range(1, 11))

for fact in factorial_expression:
    print(fact)

# Function-generator
def factorial_gen_function() -> Iterator[int]:
    for i in range(1, 11):
        yield factorial(i)

for fact in factorial_gen_function():
    print(fact)

# Class-generator
class Factorial:
    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        if self.number <= 10:
            x = factorial(self.number)
            self.number += 1
            return x
        else:
            raise StopIteration

factorial_object = Factorial()
for fact in iter(factorial_object):
    print(fact)
