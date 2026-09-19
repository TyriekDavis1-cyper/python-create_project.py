# Name: Tyriek Davis
# Date: 2026-09-09

name = input("Employee name: ")
hours = float(input("Hours Worked: "))
rate = float(input("Hourly rate of pay: "))
tax_rate = float(input("Tax Rate: "))

gross = hours * rate
tax = gross * (tax_rate/100)
net = gross * tax

print(f"Employee: {name}")
print(f"gross pay: ${gross:.2f}")
print(f"Tax withheld: ${tax:.2f}")
print(f"Net pay: ${net:.2f}")



