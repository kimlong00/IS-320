"""HW1 Problem 4, developed by Kimlong Nguyen 10.5.21.

This app compute and displays the order price 
accounting for tax, shipping,
and coffee weight of the order. 
Inputs (from user): name (str), coffee weight (float)
Outputs: total cost (float), shipping cost (float), tax (float)
"""

#inputs
name = input('What is your name?: ')
coffee_weight = float(input('How many pounds of coffee would you like to order?: '))

#initialization
coffee_unit_price = 18.50
tax_rate = 0.07
shipping_rate = 0.75

#computations
coffee_cost = (coffee_unit_price * coffee_weight) 
shipping_cost = coffee_weight * shipping_rate
tax = coffee_cost * tax_rate
total_cost = coffee_cost + shipping_cost + tax

#outputs
print(f'Hello {name:s}, you ordered {coffee_weight:.2f} pounds of coffee,')
print(f'and you owe ${total_cost:.2f}, including ${shipping_cost:.2f} for shipping, and ${tax:.2f} tax')