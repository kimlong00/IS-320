""" HW 3 Problem 4 developed by Kimlong Nguyen 10.21.21

This app takes in the number of hours worked in a week and
computes/displays the corresponding gross pay, taxes, and net pay.
The payroll guidlines concist of a base pay of $10 per hour and
an overtime rate of 1.5 times the base rate on hours above 40 per week.
Taxes are applied in brakets concisting of 15% of the first $300 earned,
20% for the next $150, and 25% for the rest.
Inputs (from user): Hours (float)
Outputs: Gross pay (float), Taxes (float), Net pay (float)
"""

#inputs
hours = float(input("Enter the number of hours worked: "))

#initializations
basic_rate = 10.0
overtime_rate = basic_rate * 1.5
tax_rate = 0.15

#computations
if hours > 40:
    gross_pay = 40 * basic_rate
    hours = hours - 40
else:
    gross_pay = hours * basic_rate
    hours = 0

if hours > 0:
    gross_pay = gross_pay + hours * overtime_rate

# Tax Tier
if gross_pay > 300:
    tax = 300 * tax_rate
    remaining_pay = gross_pay - 300
else:
    tax = gross_pay * tax_rate
    remaining_pay = 0

if remaining_pay > 150:
    tax_rate = 0.2
    tax = tax + 150 * tax_rate
    remaining_pay = remaining_pay - 150
else:
    tax_rate = 0.2
    tax = tax + remaining_pay * tax_rate
    remaining_pay = 0

if remaining_pay > 0:
    tax_rate = 0.25
    tax = tax + remaining_pay * tax_rate 

net_pay = gross_pay - tax

#outputs
print(f'\nThe gross pay for this week is ${gross_pay:.2f} \nThe taxes are ${tax:.2f} \nThe net pay is ${net_pay:.2f}')