"""Functions, Globals, Summary, Averages. Revision of: Lecture 4 App 1 

Additions: main menu

User enters weight in pounds. App computes order price,
discount, at 3% when order price is above 100$,
tax at 8%, and shipping cost.
Shipping rate is 10 cents per pound up to and including 5 pounds,
15 cents upto and including 10 pounds, and 20 cents above that.
unit price is 15$ per pound.
Display order price, discount, tax, shipping cost, and the billed amount.
('order price' above does not include tax and shipping cost.)
"""
#globals
order_count = 0 #keep track of the number of orders
total_weight  = 0.0 #sum of weights across orders
total_discount = 0.0 #track sum of discounts to compute average discount

#function
def compute_order_price(wt):
    unit_price = 15.0
    price = unit_price * wt
    
    return price

def compute_discount(price):
    global total_discount
    discount_rate = 0.3
    discount = 0.0
    if price > 100:
        discount = price * discount_rate
        total_discount = total_discount + discount

    return discount

def compute_tax(price):
    tax_rate = 0.08
    tax = price * tax_rate

    return tax

def compute_ship_rate(wt):
    ship_rate = 0.10
    if wt > 10:
        ship_rate = 0.2
    elif wt > 5:
        ship_rate = 0.15
    
    return ship_rate

def compute_ship_cost(ship_rate, wt):
    ship_cost = ship_rate * wt

    return ship_cost

def submit():
    global order_count, total_weight
    #inputs
    weight = float(input('Pounds ordered? '))

    if weight <= 0:
        print('Weight must be a positive value.')
        return

    #computations
    #1. compute price  : input: weight   output: price
    order_price = compute_order_price(weight)

    #2. compute discount, if any  : input: order price   output: discount
    discount = compute_discount(order_price)

    #3. apply discount
    order_price = order_price - discount

    #4. compute tax   input: order price  output: tax
    tax = compute_tax(order_price)

    #5. find shipping rate   input: weight  output:ship rate
    ship_rate = compute_ship_rate(weight)

    #6. find the shipping cost  input:  rate, weight   output: ship cost
    ship_cost = compute_ship_cost(ship_rate, weight)

    #7. find the billed amount
    billed = order_price + tax + ship_cost

    #update totals
    order_count = order_count + 1
    total_weight = total_weight + weight

    #outputs
    print(weight, discount, order_price, tax, ship_cost, billed)
    print()

def compute_average_weight():
    global order_count, total_weight

    if order_count > 0:
        average_weight = total_weight / order_count
    else:
        average_weight = None

    return average_weight

def compute_average_discount():
    global total_discount
    if total_discount > 0:
        average_discount = total_discount / order_count
    else:
        average_discount = None
    return average_discount

def summary():
    global order_count, total_weight

    #1. compute the average.  output: average weight float  input:
    average_weight = compute_average_weight()

    print('Summary Info:')
    if average_weight is not None:
        print(order_count, total_weight, average_weight)
    else:
        print('No data to compute average with.')
    print()

def reset():
    global order_count, total_weight

    order_count = 0
    total_weight = 0.0

#main
quit = False
while not quit: # condition applies, repeat eerthing below
    print('1.Submit 2.Summary 3.Reset 4.Quit the App')
    choice = int(input('Enter 1, 2, 3, 4:  '))

    if choice == 1:
        submit()
    elif choice == 2:
        summary()
    elif choice == 3:
        reset()
        print('Ready for a new series of inputs')
    elif choice == 4:
        quit = True #quit
    else:
        print('Invalid Choice')
#NOTES
