#!usr/bin/env python3
# Importing a random number
import random

def positive_number(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:  # even
            print(n, "is even, so divide by 2:", int(n / 2))
            n = int(n / 2)
        else:  # odd
            print(n, "is odd, use the formula 3n + 1:", int(3 * n + 1))
            n = int(3 * n + 1)
        steps += 1
    print("1")
    print("Total steps:", steps)

# Option 1: user input
num = int(input("Enter a number: "))
positive_number(num)

