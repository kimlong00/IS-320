"""
1. Inputs : income  display tax.
tax rate is 10% for income below 100,000.,
15% otherwise.

2. input: weight    display shipping cost.


3.input: score      display letter grade (A/B).
score at or above 80 gets A
others gets a B
"""

"""#Problem 1
income = 100000.0 

#computation
#   1. compute tax rate. input: income  output: tax rate floats
if income < 100000.0:  #True or false
    tax_rate = 0.1
else:
    tax_rate = 0.15


#   2. compute tax. input: income, tax rate  output: tax floats
tax = income * tax_rate


print(tax)
"""
"""
#Problem 2

weight = float(input('Enter the weight in pounds:   '))


#1. compute the ship rate. In: weight   float   out:rate float

if weight <= 10.0:
    ship_rate = 0.2
else:
    ship_rate = 0.25



#2. compute the shipping cost. in: weight(float) rate (float) out: shipping cost(float)
ship_cost = weight * ship_rate

print(f'Ship cost is {ship_cost:.2f} dollars.')
"""

#Problem 3
score = int(input('Enter the score:   '))

if score >= 80:  
    grade = 'A' # a single character is a string in python.
else:
    grade = 'B'

print(f'Score {score:d} grade {grade:s}')

#operator + - **
#comparison operators > < >= <= == !=   in general, in coding the ! symbol stands for NOT
#if x = 10:

# 'Conditions' are Expressions, they have True or False as value, type is a bool