"""Lec2App1.py Developed by KimlongN. 10.5.21.

Collects name and income from user, and displays
tax at 15% rate. Also collect and display the number of people living in the same household.
inputs: name str  income float  age int     
outputs: tax float
"""

#inputs
name = input('Enter name---> \n>')
income = float(input('Enter your income: >>'))
age = int(input('Enter your age >>'))
num_household = int(input('How many people are living in your household? >>'))

#initialization
tax_rate = 0.15

#computations
tax = income * tax_rate

#outputs
print(f'Hi {name:s}, you are {age:d} years old.') 
print(f'Your household has {num_household:d} people living there.')
print(f'Your income is ${income:.2f} dollars,')
print(f'and your your tax is ${tax:.2f} dollars')

#you are __ year old, your income is __ dollars, and your tax is ..


#NOTES
#you can split a statement by appending a \
#when you are dealing with prints,
#just use multiple print statements.
#or, use tiple quotes to print multiple lines.
#format codes for print str s

#Development Sequence:
# Variables?
#  inputs?  name str income float
#  outputs? tax float
#  anything else?   tax_rate float

#solve the problem => figure out computation steps

#code, verify, debug
#document

""" income_str = input('And your income is? >>')
#the input is '1000', a string.
#we need to extract 1000.0 from '1000'
#we convert from str to float
#float(x) will convert x to a float     : 'casting'
income = float(income_str) """