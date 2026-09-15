# Kirill M5P5 09/15/2026

# Entering last name, number if dependents, and gross income
last_name = input("Enter your last name: ")
num_depend = int(input("Enter number of dependents: "))
gross_income = float(input("Enter your gross income: "))

# Finding adjust income, by substracting gross income from muliplication of dependents on 12000
adjust_income = gross_income - (num_depend * 12000)

# if/else statment comparing adjust income with 50000
if adjust_income > 50000:
    tax_rate = 0.2
else:
    tax_rate = 0.1

# Finding income tax by multiplication of adjust income on tax rate
income_tax = adjust_income * tax_rate

# if income is less then 0, adding 100
if income_tax < 0:
    income_tax = 100

# Printing final result
print(f"Last name: {last_name}")
print(f"Gross income: ${gross_income:.2f}")
print(f"Number of dependets: {num_depend}")
print(f"Adjust gross income: ${adjust_income:.2f}")
print(f"Income tax: ${income_tax:.2f}")