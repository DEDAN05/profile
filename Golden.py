#!usr/bin/env Python3
# ASSIGNING RESTAURANT NAME
print("\n-- GOLDEN TULIP RESTAURANT--")

#USER INPUT
client_name = input("Enter your name ")
print(f"Welcome to GOLDEN TULIP {client_name}! ")


print("=====================================")


#PART 3 PRINT MENU HEAD
print(f"--------------MENU-----------")

#PART4 LIST ITEMS IN MENU
menu = [
    {"name": "PILAU", "price": 1200, "quantity": 1},
    {"name": "COFFEE", "price": 500, "quantity": 1},
    {"name": "KFC", "price": 1500, "quantity": 1},
    {"name": "PIZZA", "price": 3000, "quantity": 1},
    {"name": "WATER", "price": 250, "quantity": 1}
]

grand_total = 0

print("------ MENU ------")

for index, item in enumerate(menu, start=1):
    print(f"{index}. {item['name']} - Ksh {item['price']} - Qty: {item['quantity']}")

while True:

    choice = int(input("\nChoose item number: "))

    selected = menu[choice - 1]

    client_quantity = float(input("Enter quantity: "))

    total = selected["price"] * client_quantity

    grand_total += total

    print("\nItem:", selected["name"])
    print("Price:", selected["price"])
    print("Quantity:", client_quantity)
    print("Item Total:", total)

    another = input("\nDo you want another item? (yes/no): ")

    if another.lower() != "yes":
        break

print("\n------ FINAL BILL ------")
print("Grand Total:", grand_total)

#GETTING THE CHANGE

amount_paid = int(input("Enter amount paid by customer: "))

change = amount_paid - grand_total

print("\n------ RECEIPT ------")
print("Total Bill: Ksh", grand_total)
print("Amount Paid: Ksh", amount_paid)
print("Change: Ksh", change)
print("*" * 40)
print("\nThank you for dining with us at GOLDEN TULIP RESTAURANT!")
