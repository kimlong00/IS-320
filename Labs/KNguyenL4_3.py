#3

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
    if num_salespersons > 0 or num_salesperson_commission > 0:
        average_pay = total_pay / (num_salespersons + num_salesperson_commission)
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