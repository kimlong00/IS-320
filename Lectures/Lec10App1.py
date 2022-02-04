""" user enters:
weight in pounds,
express shipping or not.

ship rate is 20 cents per lb for weight  up to and including 20 pounds,
40 cents per lb otherwise, for standard shipping.
50 cents per pound up to and including 10 pounds, 70 cents otherwise,
for express shipping.

use two functions: compute shipping rate, and compute shipping cost.

also display: number of express shipping orders, number of standard shipping orders,
and average weight per order.
use a function to compute the average.
"""

#bool True is 1 False is 0  Anything non-zero is true.
#if <condition>
#strings and things, if empty, are False
#if income_list:    checks if income_list is not empty
#globals
express_count = 0 # number of orders with express shipping
standard_count = 0 # number of orders with standard shipping
total_weight = 0.0 # sum of weights, to compute the average weight
weight_list = [] # a list to store all the input weight

#functions

def compute_ship_rate(weight, express):
    global express_count, standard_count, total_weight
    
    if express:
        express_count += 1
        if weight <= 10.0:
            rate = 0.5
        else:
            rate = 0.7
    else:
        standard_count += 1
        if weight <= 20.0:
            rate = 0.2
        else:
            rate = 0.4

    return rate

def compute_ship_cost(weight, rate):
    global express_count, standard_count, total_weight
    
    cost = weight * rate

    return  cost

def submit():
    global express_count, standard_count, total_weight
    #inputs
    weight = float(input('Enter weight in pounds: '))
    express = int(input('Enter 1 for express 0 standard shipping: ')) #1  express 0 standard

    #computations
    ship_rate = compute_ship_rate(weight, express)
    ship_cost = compute_ship_cost(weight, ship_rate)

    #updates
    total_weight += weight
    weight_list.append(weight)

    #outputs
    print(weight, express, ship_rate, ship_cost)

def compute_average_weight():
    global express_count, standard_count, total_weight

    if express_count or standard_count:
        average_weight = total_weight / (express_count + standard_count)
    else:
        average_weight = None
    
    return average_weight

def summary():
    global express_count, standard_count, total_weight
    
    average_weight = compute_average_weight()
    if average_weight is not None:
        print(total_weight, express_count, standard_count, average_weight)
    else:
        print('No Data!')

def reset():
    global express_count, standard_count, total_weight

    express_count = 0
    standard_count = 0
    total_weight = 0.0
    weight_list.clear()

def display():
    global express_count, standard_count, total_weight
    if weight_list:
        print('----------------')
        print('Weight in pounds')
        print('----------------')
        for wt in weight_list:
            print(f'{wt:.2f}')
        print('----------------')
    else:
        print('No orders to display!')

#main
quit = False
while not quit: # condition applies, repeat eerthing below
    print('1.Submit 2.Summary 3.Reset 4.Display all orders 5.Quit the App')
    choice = int(input('Enter 1, 2, 3, 4, 5:  '))

    if choice == 1:
        submit()
    elif choice == 2:
        summary()
    elif choice == 3:
        reset()
        print('Ready for a new series of inputs')
    elif choice == 4:
        display()
    elif choice == 5:
        quit = True #quit
        weight_list.clear()
    else:
        print('Invalid Choice')


# [10, 20, 40]
# make a list
# add an item to the list
# weight_list.append to the list
# display contents of the list:

# empty out the list
# weight_list.clear()

# 7pm Thursday
# 9pm Friday

weight_list = [1, 9, 3]
print(weight_list[1])
weight_list.clear()
weight_list.append(100)
print(weight_list[0])