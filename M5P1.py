# Kirill M5P1 09/15/2026

# Entering a quantity of item 
quantity = float(input("Enter quantity of item: "))

# Comparing quantity with 1000
if quantity >= 1000:
    unit_price = 3
else:
    unit_price = 5

# Calculation of tax and final price
extended_price = quantity * unit_price
tax = extended_price * 0.07
total = tax + extended_price

# Printing result
print(f"Quantity: {quantity}")
print(f"Unit price: ${unit_price}")
print(f"Extended price: ${extended_price}") 
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")