""" HW 3 Problem 5 developed by Kimlong Nguyen 10.21.21

This app takes in the income, married status and
the number of exemptions and calculates the corresponding taxes.
Any individuals can claim up to a maximum of 3 exemptions.
Single exemptions are worth $375 each while married are $500 each.
Total exemptions are subtracted from the income to make taxable income.
Single income rate is 18% for amounts above $100,000 and 15% for other.
Married income rate is 30% for amounts above $150,000 and 20% for other.
Inputs (from user): Income (float), married status (int/bool), exemptions (int)
Outputs: Tax (float)
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

def compute_tax_single(income):
    if income > 100000:
        tax = income * 0.18
    else:
        tax = income * tax_rate_single    
    
    return tax

def compute_tax_married(income):
    if income > 150000:
        tax = income * 0.30
    else:
        tax = income * tax_rate_married    
    
    return tax

if not married:
    taxable_income = income - deductable_exemptions * single_exemption_rate
    tax = compute_tax_single(taxable_income)
else:
    taxable_income = income - deductable_exemptions * married_exemption_rate
    tax = compute_tax_married(taxable_income)

#outputs
if married:
    print('\nMarried:')
else:
    print('\nSingle:')

print(f'Income: ${income:.2f} \n{exemptions:d} Exemptions \nTax is ${tax:.2f}')