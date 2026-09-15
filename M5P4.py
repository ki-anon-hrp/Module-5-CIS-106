# Kirill M5P4 09/15/2026

# Asking user to enter their appliance and it cost
name_appliance = input("Enter name of your appliance: ")
cost_appliance = float(input("Enter cost of your appliance: "))

# Comparing cost with 1000 and giving a suitable warranty
if cost_appliance > 1000:
   warranty = 0.1
else:
   warranty = 0.05

# Calculate total a price, by multiply cost appliance on warranty and additing cost
total = (cost_appliance * warranty) + cost_appliance

# Printing final result
print(f"Appliance: {name_appliance}") 
print(f"Cost: ${cost_appliance}") 
print(f"Warranty: {cost_appliance * warranty:.2f}")
print(f"Warranty with {warranty}%: ${total:.2f}")