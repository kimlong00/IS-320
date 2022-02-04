#3

#inputs
sales = float(input("Enter the weekly sales: "))

#initializations
base_salary = 250
commision_rate = 0.15
commission = 0.0

#computations
if sales >= 1000:
    commission = commision_rate * sales

total_earnings = base_salary + commission

#outputs
if commission > 0:
    print(f'Total commission for this week is ${commission:.2f} and total pay is ${total_earnings:.2f}')
else:
    print(f'Total pay for this week is ${total_earnings:.2f}')