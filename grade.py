import random
name = input("Enter your name: ")
print(f"my name is {name} and a filling the numbers")
def positive_number(n):
    steps = 0 
    while n != 1 :
        if n % 2 == 0: #even
            print(n, "is even, Divide by 2 again", (n / 2))
            n = int(n / 2)
    else:
        print(n, "is odd number, so i divide 3n + 1", (3 * n + 1))
        n = int(3 * n + 1)
    steps += 1
    print("1")
    print("Total steps:", steps)

    # finding the calculations 
num = int(input("Enter a number: "))
positive_number(num)
