def greet(fname, lname):
    print("Hello, World!")
    print("This is my first function")
    print(f"Welcome {fname} {lname} to python")

greet("John", "Doe")

def increment(x=5,y=2):
    value = x + y
    print(value)

increment()
# ARGYS
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
        print(total)

add(1, 3, 5)

#**KWARGYS
def get_bio(**info):
    print("Bio Information: ")
    for key, value in info.items():
         print(f"{key}: {value}")


get_bio(name="John Doe", profession="cyebersecurity analyst", Age="25", Titles="Engineer" )
