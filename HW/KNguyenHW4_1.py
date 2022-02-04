"""HW 4 Problem 1 developed by Kimlong Nguyen 10.28.21

This app takes in the number of books ordered and whether
the order is online or not. Each book cost $15 and if the order
is offline, a tax rate of 8% is applied. If the order is online,
the shipping rate is 25 cents up to 10 books, after that,
a shipping flat rate of $5 for the order.
Inputs (from user): Number of books (int), order type (int/bool)
Outputs: The order price with shipping and taxes (float), average revenue (float)
"""

#global variables
revenue = 0.0 #sum of total amount of revenue
num_online_orders = 0 #Keeps track the number of online orders
num_offline_orders = 0 #Keeps track the number of ofline orders

#functions
def compute_shipping_cost(n_books):
    if n_books > 10:
        shipping_cost = 5.0
    else:
        shipping_rate = 0.25
        shipping_cost = n_books * shipping_rate
    
    return shipping_cost

def compute_tax(order_rev):
    tax_rate = 0.08
    tax = order_rev * tax_rate

    return tax

def compute_average_revenue():
    if num_offline_orders > 0 or num_online_orders > 0:
        average_rev = revenue / (num_offline_orders + num_online_orders)
    else:
        average_rev = None
    
    return average_rev

def submit():
    global num_online_orders, num_offline_orders, revenue

    #inputs
    num_books = int(input('Enter the number of books ordered: '))
    order_online = int(input('Is the the book online(1) or offline(0): '))

    #computations
    order_revenue = num_books * 15

    if order_online:
        shipping_cost = compute_shipping_cost(num_books)
        order_price = order_revenue + shipping_cost
        num_online_orders += 1
    else:
        tax = compute_tax(order_revenue)
        order_price = order_revenue + tax
        num_offline_orders += 1

    #updates
    revenue += order_revenue

    #outputs
    print(f'Total order price including taxes and shipping: ${order_price:.2f}\n')

def summary():
    average_revenue = compute_average_revenue()
    if average_revenue is None:
        print('No inputs were entered')
    else:
        print(f'Number of offline orders: {num_offline_orders:d}')
        print(f'Number of online orders: {num_online_orders:d}')
        print(f'Average revenue: {average_revenue:.2f}')

#main
summary()
submit()
submit()
submit()
summary()