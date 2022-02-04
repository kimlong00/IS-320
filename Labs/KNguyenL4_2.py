#2

#global
num_married = 0 #keep track the number of married filers
num_unmarried = 0 #keep track the number of unmarried filers
total_tax = 0 #sum of the total amount of tax across all filers

#functions
def compute_deductable_exemptions(exemp):
    if exemp > 3:
        deductable_exemptions = 3
    else:
        deductable_exemptions = exemp

    return deductable_exemptions

def compute_taxable_income(income, deduct, married):
    global num_married, num_unmarried
    if married:
        taxable_income = income - deduct * 500
        num_married += 1
    else:
        taxable_income = income - deduct * 375
        num_unmarried += 1

    return taxable_income

def compute_tax_rate(income, married):
    if married:
        if income > 150000:
            tax_rate =  0.30
        else:
            tax_rate = 0.2
    else:
        if income > 100000:
            tax_rate = 0.18
        else:
            tax_rate = 0.15
    
    return tax_rate

def compute_average_tax():
    average_tax = total_tax / (num_married + num_unmarried)

    return average_tax

def submit():
    global total_tax
    #inputs
    income = float(input('Enter your income: '))
    married = int(input('Are you married? yes(1) no(0): '))
    exemptions = int(input('How many claimed exemptions?: '))

    #computations
    #process current inputs
    deductable_exmpetions = compute_deductable_exemptions(exemptions)
    taxable_income = compute_taxable_income(income, deductable_exmpetions, married)
    tax_rate = compute_tax_rate(taxable_income, married)
    tax = tax_rate * taxable_income
    total_tax += tax

    #outputs:
    if married:
        print('\nMarried:')
    else:
        print('\nSingle:')

    print(f'Income: ${income:.2f} \n{exemptions:d} Exemptions \nTax is ${tax:.2f}')

def summary():
    average_tax = compute_average_tax()
    print(f'Number of married taxpayers: {num_married:d}')
    print(f'Number of unmarried taxpayers: {num_unmarried:d}')
    print(total_tax)
    print(f'Average tax: ${average_tax:.2f}')
    

#main
submit()
submit()
submit()
summary()