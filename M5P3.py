# Kirill M5P3.py 09/15/2026

# Entering amount of books and cost
books = int(input("Enter amount of books you ordered: "))
cost_books = float(input("Enter cost per book: "))

# Multiply amount of books on cost
total = books * cost_books

# if/else statement comparing total price with 50
if total > 50:
    shipping = 0
else: 
    shipping = 25

#Printing shipping and total cost
print(f"Cost of shipping: ${shipping}")
print(f"Total cost: ${total + shipping}")