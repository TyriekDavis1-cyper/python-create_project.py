# Name:Tyriek Davis
# Date:2026-09-09
# Course: COMP 163
# Project 1: Paycheck Calculator

name = input("Employee name: ")
hours = float(input("Hours worked: "))
tax_rate = float(input("Tax rate: "))

gross = hours * rate
tax = gross * (tax_rate / 100)
net = gross - tax

print(f"Employee: {name}")
print(f"Gross pay: ${gross:.2f}")
print(f"Tax withheld: ${tax:.2f}")
print(f"Net pay: ${net:.2f}")
