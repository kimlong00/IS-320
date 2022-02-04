#1.

#inputs
married = str.lower(input('Are you married? (y/n): '))
income = float(input('What is your income?: '))

#initializations
tax_rate = 0.10

#computations
if married == 'y':
    if income > 200000:
        tax_rate = 0.20
    else:
        tax_rate = 0.15
elif income > 100000:
    tax_rate = 0.15

tax = tax_rate * income

#output
print(tax_rate)
print(f'Total tax: ${tax:.2f}')