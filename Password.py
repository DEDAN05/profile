#! usr/bin/env python3
import random
import string
#printing the titile of the program
print("================Password Generator===================")
print( )
#asking the user for the length of the password
password_length = int(input("Enter the length of the password: "))
if password_length >= 8 and password_length <= 16:
    print(f"password lenth is: {password_length}")
else:
    print("Password length should be between 8 and 16 characters.")
#asking the user for the type of characters to include in the password  
print("Select the type of characters to include in the password:")
print("1. Uppercase letters")
print("2. Lowercase letters")
print("3. Digits")
print("4. Special characters")
character_types = input("Enter the numbers corresponding to the character types (e.g., 1,2,3): ")
#creating a variable to store the chara,3,cters to be included in the password 
characters = ""
if '1' in character_types:
    characters += string.ascii_uppercase
if '2' in character_types:
    characters += string.ascii_lowercase
if '3' in character_types:
    characters += string.digits
if '4' in character_types:
    characters += string.punctuation  
#generating the password using random.choices() function
password = ''.join(random.choices(characters, k=password_length))  
print(f"Generated password: {password}")
