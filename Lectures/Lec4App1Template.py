"""Lecture 4 App 1.  Price computation.

User enters weight in pounds. App computes order price,
discount, at 3% when order price is above 100$,
tax at 8%, and shipping cost.
Shipping rate is 10 cents per pound up to and including 5 pounds,
15 cents upto and including 10 pounds, and 20 cents above that.
unit price is 15$ per pound.
Display order price, discount, tax, shipping cost, and the billed amount.
('order price' above does not include tax and shipping cost.)
input: weight float
output: order price, discount, tax, shipping cost, billed amount - all float
"""

#inputs
weight = float(input('Enter weight, in pounds: >>'))

#initializations
unit_price = 15.0
discount_rate = 0.03
tax_rate = 0.08
discount = 0.0
#(note)default value used to eliminate the else below

#computations
#   1. compute order price  input: weight float   output: price float
order_price = weight * unit_price
#   2. compute discount, if any.  input: price float    output: discount float
if order_price > 100:
    discount = order_price * discount_rate

#   3. apply the discount
order_price = order_price - discount
#   4. compute the tax.  input: price float  output: tax
tax = order_price * tax_rate

#   5. compute shipping rate  input: weight float  output: ship rate float
if weight <= 5.0:
    ship_rate = .10
elif weight <= 10.0:
    ship_rate = 0.15
else:
    ship_rate = 0.20

#   6. compute shipping cost input: weight, rate floats  output: ship cost float
ship_cost = weight * ship_rate
#   7. compute the billed amount
billed_amount = order_price + tax + ship_cost
#outputs
print(weight, discount, order_price, tax, ship_cost, billed_amount)
#DIY insert text and formatting


#SEQUENCE (for developing an app)

#what are the variables? and their types?
#inputs?
#outputs?
#any other variables?
#   what is known already (given constants)
#   other intermediate results

# read inputs
# solve the problem in stages
# code and verify in stages
# document and organize code as needed


#efficiency - conserve resources:
#primary resources used by a program are:
#   cpu - computing power - reduce number of statements
#   memory - reduce number of variables

#review your code:
#1. unused variables?
#2. variables that I use, but were not really needed?
#3. redundant steps

#The else below does nothing. Discard!
#  if price > 100:
#     discount = ....
#  else:
#     discount = discount

#use parentheses only if absolutely must use them.  (in functions, and to change the order of precedence)

#NOTES FOR LATER   AND OR :  
# briefly: and  or   can be used to combine conditions. but don't use them yet.
# 
# details: 
# score >= 0 and score <= 100       score < 0  or score > 100
# Not:  score >= 0 and <= 100 !
# and :  both conditions must be True
# or: one or more conditions to be true
# if mixing and, or in an expression (such as A and B or C), use parentheses.


#Alternatives:

# for most problems, the if statement can be written without use of and/or.
# the chance of errors, and the chance of inefficiency (and chance of losing points)
# is higher when you use and/or.  recommend you avoid using them till later.

# and -  same as nested if.
#if score >= 0:
#   if score <= 100:
#      ....
#or -  same as an if..elif with the same action under both 
#if score < 0:
#   print('invalid!')
#elif score > 100:
#   print('invalid!')

#these alternatives (nested if and elif) usually work better for efficiency and
#accuracy for beginners. 

#Going further:
# A and B:    since both A and B need to be True, if A fails, there is no point in
# checking B.  Python will stop evaluating if A is False. 
#A or B:  since only one needs to be true, if A is true, there is no point in checking
#B.  Python will stop evaluating if A is true.
#this is referred to as: 'short circuit evaluation'.

#in turn, in A and B, if evaluation reaches B, you know A is True
#in A or B, if evaluation reaches B, you know A is False.

#logic practice:
#Try to simplify:  
#why simplify? reducing number of conditions evaluated improves efficiency
#A and (A or B)
#A and (not A or B)       not A means reverse of A
#A or (A and B)
#A or (not A and B)

