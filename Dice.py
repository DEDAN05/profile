#!usr/bin/env python3
import random
print("*" * 40)
print("     THE DICE ROLLER GAME   ")
print("*" * 40)
name = input("Enter your name: ")
print(f"Hello {name}, welcome to the Dice Roller Game!")

while True:
    print()
    try:
        sides = int(input("Enter the number of sides on the die (or '0' to quit): "))
        if sides == 0:
            print(" ")
            print("TRY AGAIN!")
            continue

            

        elif sides < 1:
            print(" ")
            print("Please enter a positive number for the number dice sides.")
            continue
        
            
        else:
            results = random.randint(1, sides)
            print(" ")
            print(f"Your roll is {results} out of {sides} sided die.")
            break


    except ValueError:
        print(" ")
        print("Invalid input. Please enter a valid number of sides on your die.")
        
print("*****************RECEIPT OF ALL ROLLS*****************")
print(f"Player Name: {name}")
print(f"your results is: {results}")
print(f"No of sides on the die: {sides}")



