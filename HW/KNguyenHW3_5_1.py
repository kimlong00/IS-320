""" HW 3 Problem 5 developed by Kimlong Nguyen 10.21.21

This app computes

"""

#inputs
income = float(input('Enter your income: '))
married = int(input('Are you married? yes(1) no(0): '))
exemptions = int(input('How many claimed exemptions?: '))

#initializations
single_exemption_rate = 375.0
married_exemption_rate = 500.0
tax_rate_single = 0.15
tax_rate_married = 0.2

#computations
if exemptions > 3:
    deductable_exemptions = 3
else:
    deductable_exemptions = exemptions

if not married:
    taxable_income = income - deductable_exemptions * single_exemption_rate
    if taxable_income > 100000:
        tax = 100000 * tax_rate_single
        taxable_income = taxable_income - 100000
        tax = tax + taxable_income * 0.18
    else:
        tax = taxable_income * tax_rate_single
else:
    taxable_income = income - deductable_exemptions * married_exemption_rate
    if taxable_income > 150000:
        tax = 150000 * tax_rate_married
        taxable_income = taxable_income - 150000
        tax = tax + taxable_income * 0.30
    else:
        tax = taxable_income * tax_rate_married

#outputs
if married:
    print('\nMarried:')
else:
    print('\nSingle:')

print(f'Income: ${income:.2f}')
print(f'{exemptions:d} Exemptions')
print(f'Tax is ${tax:.2f}')