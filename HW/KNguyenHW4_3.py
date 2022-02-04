"""HW 4 Problem 3 developed by Kimlong Nguyen 10.28.21

This app takes in the number of sales for the week for each salesperson
and computes the total pay, average pay among all salepersons,
and the number of salespersons and the number of commisions. 
If weekly sales are above 1000, an extra 15% rate commision is applied.
Input (from user): number of weekly sales (int)
Output: Total pay (float), Average pay (float), Number of salesperson (int), 
Number of salepersons earning commision (int)
"""

#globals
num_salespersons = 0 #keep track the number of salespersons
num_salesperson_commission = 0 # keep track the number of salesperson with commisions
total_pay = 0.0 #sum of the total pay across all salespersons

def compute_commision(sales):
    global num_salespersons, num_salesperson_commission
    if sales >= 1000:
        commision_rate = 0.15
        commission = commision_rate * sales
        num_salesperson_commission += 1
    else:
        commission = 0

    num_salespersons += 1
    return commission

def compute_average_pay():
    if num_salespersons > 0:
        average_pay = total_pay / num_salespersons
    else:
        average_pay = None

    return average_pay

def submit():
    global total_pay

    #inputs
    sales = float(input("Enter the weekly sales: "))

    #computations
    commission = compute_commision(sales)
    earnings = 250 + commission
    
    #updates
    total_pay += earnings

    #outputs
    if commission > 0:
        print(f'Total commission for this week is ${commission:.2f} and total pay is ${earnings:.2f}')
    else:
        print(f'Total pay for this week is ${earnings:.2f}')

def summary():
    average_pay = compute_average_pay()
    
    if average_pay is None:
        print('No inputs were entered')
    else:
        print(f'Average pay: ${average_pay:.2f} \nNumber of salespersons: {num_salespersons:d}')
        print(f'Number of salespersons earning commission: {num_salesperson_commission:d}')

#main
summary()
submit()
submit()
submit()
summary()