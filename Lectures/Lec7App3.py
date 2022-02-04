"""Lecture 7 App, Global variables, submit, summary functions.

User enters income.  Taxed at 15% if above 100,000 else 10%.
Display tax,
and average tax.
"""
#global variables
total_tax = 0.0 #tracking sum of taxes to compute average with.
num_inputs = 0 #count the number of inputs, for use with average tax
count_hi_earners = 0 # number of taxpayers with income above 100k

#functions
def compute_tax_rate(inc):
    global count_hi_earners

    if inc > 100000.0:
        rate = 0.15
        count_hi_earners = count_hi_earners + 1
    else:
        rate = 0.1

    return rate

def compute_tax(inc, rt):
    tax = inc * rt

    return tax

def submit():
    global total_tax, num_inputs, count_hi_earners
    
    #inputs
    income = float(input('Enter income>>> '))

    #computations
    #process current inputs
    # 1. compute the tax rate. out: tax rate  float  in: income
    tax_rate = compute_tax_rate(income)   #inc = 200000.0

    # 2. compute the tax. out: tax  float  in: income, tax_rate
    tax = compute_tax(income, tax_rate)

    #update totals
    total_tax = total_tax + tax
    num_inputs += 1  #num_inputs = num_inputs + 1
   

    #outputs
    print(income,  tax)

def summary():
    global total_tax,num_inputs

    average_tax = total_tax / num_inputs

    print(f'{total_tax:.2f}, {num_inputs:d}, {average_tax:.2f}')
    


#main
submit()
submit()
summary()
submit()
summary()


#NOTES
#average tax = total tax / number of inputs
#=> keep track of: total tax and number of inputs
# keep track of: => use a variable.
#total_tax float. 
#num_inputs int

#fewest possible global variables

#count high earners and low earners

#globals:   1. remember their value after function is over 
#           2. can be seen by all functions.

#criteria for making variables global: if one of the above is needed.

