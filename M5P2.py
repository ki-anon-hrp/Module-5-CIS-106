# Kirill M5P2 09/15/2026

# Entering an iteam and a quantity
iteam = (input("Enter a name of the item (A or B): "))
quantity = int(input("Enter a quantity of the item: "))

# if/else iteam is A, unit price is 10, else unit price is 20
if iteam == "A":
    unit_price = 10
else: 
    unit_price = 20

# Multiplication of quantity on unit price
extended_price = quantity * unit_price

# Printing iteam, quantity, unit price, and extended price
print(f"Iteam: {iteam}") 
print(f"Quantity: {quantity}")
print(f"Unit price: ${unit_price:.2f}")
print(f"Extended price: ${extended_price:.2f}")