"""HW 2 Problem 1 developed by Kimlong Nguyen 10.14.21

This app computes and displays the order cost of the order
before and after shipping cost are applied
given the inputs of various vegetables in pounds. 
Inputs (from User): Atichokes, carrots, beets all in pounds (float)
Outputs: The order cost before and after shipping cost (float), shipping cost (float)
"""

#inputs
artichokes_pounds = float(input('How many pounds of artichokes: '))
carrots_pounds = float(input('How many pounds of carrots: '))
beets_pounds = float(input('How many pounds of beets: '))

#initializations
artichokes_unit = 2.67
carrots_unit = 1.49
beets_unit = 0.67
discount_rate = 0.05
discount = 0.0

#computations
total_weight = artichokes_pounds + carrots_pounds + beets_pounds
cost_before_shipping = artichokes_unit * artichokes_pounds + carrots_unit * carrots_pounds + beets_unit * beets_pounds

if cost_before_shipping > 100:
    discount = cost_before_shipping * discount_rate

cost_before_shipping = cost_before_shipping - discount

if total_weight < 5:
    shipping_cost = 3.50
elif total_weight < 20:
    shipping_cost = 10
else:
    shipping_cost = 9.5 + total_weight * 0.10

total_cost = cost_before_shipping + shipping_cost

#outputs
print(f'The order cost before shipping is ${cost_before_shipping:.2f}')
print(f'The shipping cost is ${shipping_cost:.2f}')
print(f'The total cost is ${total_cost:.2f}')
