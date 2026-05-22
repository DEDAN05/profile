# DUKA SMART BILLING SYSTEM

# PART 1 — CUSTOMER DETAILS
customer_name = input("Enter customer name: ")
age = int(input("Enter customer age: "))

print(f"\nWelcome to Duka Smart, {customer_name}! (Age: {age})")

# PART 2 — ITEM DETAILS

# Item 1
item1 = input("\nEnter item 1 name: ")
qty1 = int(input("Enter quantity for item 1: "))
price1 = float(input("Enter price for item 1: "))
total1 = qty1 * price1

# Item 2
item2 = input("\nEnter item 2 name: ")
qty2 = int(input("Enter quantity for item 2: "))
price2 = float(input("Enter price for item 2: "))
total2 = qty2 * price2

# Item 3
item3 = input("\nEnter item 3 name: ")
qty3 = int(input("Enter quantity for item 3: "))
price3 = float(input("Enter price for item 3: "))
total3 = qty3 * price3

# PART 3 — CALCULATIONS
subtotal = total1 + total2 + total3
vat = subtotal * 0.16
grand_total = subtotal + vat

# PRINT RECEIPT
print("\n--- RECEIPT ---\n")

print(f"1. {item1:<15} x{qty1}  =  KES {total1:.2f}")
print(f"2. {item2:<15} x{qty2}  =  KES {total2:.2f}")
print(f"3. {item3:<15} x{qty3}  =  KES {total3:.2f}")

print("\nSubtotal  :  KES {:.2f}".format(subtotal))
print("VAT (16%) :  KES {:.2f}".format(vat))
print("TOTAL     :  KES {:.2f}".format(grand_total))

# PART 4 — CHANGE CALCULATOR
cash = float(input("\nEnter cash paid: "))

if cash >= grand_total:
    change = cash - grand_total
    print("\nCash paid :  KES {:.2f}".format(cash))
    print("Change    :  KES {:.2f}".format(change))
else:
    shortfall = grand_total - cash
    print("\nInsufficient cash.")
    print("Shortfall :  KES {:.2f}".format(shortfall))

    
    print("\nThank you for Shopping at DUKA SMART!")