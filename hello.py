#!/usr/bin/env python3
# DUKA SMART BILLING SYSTEM

# PART 1 — CUSTOMER DETAILS
customer_name = input("Enter customer name: ")
age = int(input("Enter customer age: "))

print("\nWelcome", customer_name + "!")
print("Age:", age)
print("--------------------------------")

# PART 2 — ITEM 1
item1 = input("Enter item 1 name: ")
qty1 = int(input("Enter quantity for item 1: "))
price1 = float(input("Enter price for item 1 in KES: "))

total1 = qty1 * price1

# ITEM 2
item2 = input("\nEnter item 2 name: ")
qty2 = int(input("Enter quantity for item 2: "))
price2 = float(input("Enter price for item 2 in KES: "))

total2 = qty2 * price2

# ITEM 3
item3 = input("\nEnter item 3 name: ")
qty3 = int(input("Enter quantity for item 3: "))
price3 = float(input("Enter price for item 3 in KES: "))

total3 = qty3 * price3

# PART 3 — CALCULATIONS
subtotal = total1 + total2 + total3
vat = subtotal * 0.16
grand_total = subtotal + vat

# PRINT RECEIPT
print("\n================================")
print("       DUKA SMART RECEIPT")
print("================================")

print("Customer:", customer_name)
print("--------------------------------")

print(item1, "x", qty1, "KES", total1)
print(item2, "x", qty2, "KES", total2)
print(item3, "x", qty3, "KES", total3)

print("--------------------------------")
print("Subtotal: KES", subtotal)
print("VAT (16%): KES", vat)
print("Grand Total: KES", grand_total)
print("================================")

# PART 4 — CHANGE CALCULATOR
cash = float(input("\nEnter cash paid: "))

if cash >= grand_total:
    change = cash - grand_total
    print("Change due: KES", change)
else:
    shortfall = grand_total - cash
    print("Insufficient cash.")
    print("Add KES", shortfall, "more.")

print("\nThank you for shopping at Duka Smart!")