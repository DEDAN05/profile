#! usr/bin/env python3
print("*" * 40)
print("     WELCOME TO THE NIMM  MIND GAME   ")
print("*" * 40)
name = input("Enter the name of the player A: ")
name2 = input("Enter the name of the player B: ")
print(f"Hello {name} and {name2}, welcome to the NIMM MIND GAME!")
print(" ")
print("the rules of the game are as follows:")
print("You can take 1, or 2 from the pile of 20,"
"the player who takes the last one loses the game")

#Assigning the number of stones
stone = 20
while True:     
    print(" ")
    try:
        playerA = int(input(f"{name} enter the number of stones you want to take (1 or 2): "))
        if playerA not in [1, 2]:
            print(" ")
            print("Invalid input. Please enter either 1 or 2.")
            continue
        stone -= playerA
        print(f"Stones left: {stone}")
        if stone <= 0:
            print(f"{name} took the last stone. {name2} wins!")
            break

        playerB = int(input(f"{name2} enter the number of stones you want to take (1 or 2): "))
        if playerB not in [1, 2]:
            print(" ")
            print("Invalid input. Please enter either 1 or 2.")
            continue
        stone -= playerB
        print(f"Stones left: {stone}")
        if stone <= 0:
            print(f"{name2} took the last stone. You lost the game. {name} wins!")
            break

    except ValueError:
        print(" ")
        print("Invalid input. Please enter a valid number of stones to take.")