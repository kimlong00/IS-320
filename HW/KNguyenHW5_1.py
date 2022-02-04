"""HW5 Problem 1 Developed by Kimlong Nguyen 11.15.21

This app depicts a gas filling app where users can choose the gas grade,
and fills their car with a certain ammount of gas (gallons). 
The app also allows the manager to change the prices of each grade of gas
as well as see the total amount of sales and gallons sold in a day.
The manager also has the ability to reset the information for the next day.

Inputs: gas grade (int) gallons (float) confirmations (int)

Outputs: price (float) gallons (float) sales (float)
"""

#globals
regular_gallons = 0.0 # count the total amount of regular gas gallons sold
extra_gallons = 0.0 # count the total amount of extra gas gallons sold
premium_gallons = 0.0 # count the total amount of premium gas gallons sold
regular_price = 3.7 # keep track of the price for regular gas
extra_price = 3.9 # keep track of the price for extra gas
premium_price = 4.1 # keep track of the price for premium gas
total_sales = 0.0 # count the total amount of gallons sold

#functions
def is_valid_grade(grade):
    """Boolean function to check if inputed gas grade is valid 1,2,3
    
    Parameter:
        grade (int)
    Return:
        Boolean
    """

    return grade > 0 and grade < 4

def is_valid_gas_price(price):
    """Boolean function to check if price is valid (above 0)
    
    Parameter:
        price (float)
    Return:
        Boolean
    """

    return price > 0

def compute_price(gallons, gas_rate):
    """Computes the price of order when given the number of gallons and unit price of the gas
    
    Paramter:
        gallons (float) gas rate (float)
    Return:
        price (float)
    """

    global total_sales, regular_gallons, extra_gallons, premium_gallons, regular_price, extra_price, premium_price
    
    price = gallons * gas_rate
    total_sales += price
    
    return price

def update_gallons(gallons, grade):
    """Updates the ammount of gallons for the specified gas grade within the global variables
    
    Paramters:
        gallons (float) gas grade (int)
    Return:
        None
    """

    global total_sales, regular_gallons, extra_gallons, premium_gallons, regular_price, extra_price, premium_price
    
    if grade == 1:
        regular_gallons += gallons
    elif grade == 2:
        extra_gallons += gallons
    else:
        premium_gallons += gallons

def fill():
    """Display the user with the prices per gallon for each type of gas
    Prompt the with the type of gas and the ammount of gas they are filling up.

    Parameter:
        None
    Return:
        None
    User Inputs:
        gas type (int) gallon (float)
    Display:
        Gas grade prices and selection

    """

    global total_sales, regular_gallons, extra_gallons, premium_gallons, regular_price, extra_price, premium_price
    
    line()
    print('Prices: Regular: Extra: Premium:')
    print(f'$Per Gallon: {regular_price:.2f}: {extra_price:.2f}: {premium_price:.2f}')
    print('Choose 1.Regular 2.Extra or 3.Premium')
    line()

    gas_type = int(input('1/2/3:  '))

    if gas_type == 1:
        grade = 'Regular'
        gas_rate = regular_price
    elif gas_type == 2:
        grade = 'Extra'
        gas_rate = extra_price
    elif gas_type == 3:
        grade = 'Premium'
        gas_rate = premium_price
    else:
        print('Please enter an appropriate value (1,2,3)')
        return
    
    print(f'Your selection: {grade:s} ${gas_rate:.2f} per gallon')
    gallons = float(input('Enter how many gallons to fill: '))

    if gallons == 0:
        print('Operation Cancelled:')
        return
    elif gallons < 0:
        print('Please enter a positive number')
        return

    #computations
    price = compute_price(gallons, gas_rate)

    #updates
    update_gallons(gallons, gas_type)

    #outputs
    print(f'Total price for {gallons:.2f} gallons of {grade:s} gas is: ${price:.2f}')

def line():
    print('-' * 38)

def sales():
    """Displays the total number of gallons sold of each grade of fuel
    
    Parameters:
        None
    Return:
        None
    Display:
        Current gas grade price and total sales
    """

    global total_sales, regular_gallons, extra_gallons, premium_gallons, regular_price, extra_price, premium_price
    
    line()
    print('Gallons sold: Regular: Extra: Premium:')
    print(f'{"Total":12s}: {regular_gallons:.2f}: {extra_gallons:.2f}: {premium_gallons:.2f}:')
    print(f'Total Sales : ${total_sales:.2f}')
    line()

def prices():
    """Displays the user with the prices for each grade of gas.
    Prompts the user with new price inputs for each grade of gas.
    After prompting every gas option, confirms with the user for change and updates the corresponding globals.
    
    Parameters:
        None
    Returns:
        None (if not invalid)
    Inputs:
        regular price (string) extra price (string) premium price (string)
    Displays:
        Current gas grade prices and selection
        """

    global total_sales, regular_gallons, extra_gallons, premium_gallons, regular_price, extra_price, premium_price
    
    line()
    print('Prices: Regular: Extra: Premium:')
    print(f'$Per Gallon: {regular_price:.2f}: {extra_price:.2f}: {premium_price:.2f}:')
    print('For each grade, when prompted, enter new price, or hit Return if price stays same')
    line()

    new_regular = input('Enter a new price for Regular: ')
    if new_regular and not is_valid_gas_price(float(new_regular)):
        print('Invalid Input: Please enter a positive value greater than 0!')
        return

    new_extra = input('Enter a new price for Extra: ')
    if new_extra and not is_valid_gas_price(float(new_extra)):
        print('Invalid Input: Please enter a positive value greater than 0!')
        return

    new_premium = input('Enter a new price for Premium: ')
    if new_premium and not is_valid_gas_price(float(new_premium)):
            print('Invalid Input: Please enter a positive value greater than 0!')
            return
    
    confirm_prices = int(input('Enter 1 to confirm change of prices, 0 to cancel: '))

    if not confirm_prices:
        return

    #updates
    if new_regular:
        regular_price = float(new_regular)
    
    if new_extra:
        extra_price = float(new_extra)
    
    if new_premium:
        premium_price = float(new_premium)

    print('Prices: Regular: Extra: Premium:')
    print(f'$Per Gallon: {regular_price:.2f}: {extra_price:.2f}: {premium_price:.2f}:')
    
def end_of_day():
    """Displays the sales information function as well as prompt the user with the option to reset information.
    Information includes the ammount of gallons sold and the total number of sales for the day.

    Parameter:
        None
    Return:
        None
    User Inputs:
        reset (int)
    Display:
        Current gas grade price, total sales, and selection
    """

    global total_sales, regular_gallons, extra_gallons, premium_gallons, regular_price, extra_price, premium_price
    sales()
    reset = int(input('Do you want to reset information? 1 = yes, 0 = no: '))
    
    if reset:
        regular_gallons = 0.0
        extra_gallons = 0.0
        premium_gallons = 0.0
        total_sales = 0.0

#main
quit = False
while not quit:
  print('\n1.Fill 2.Sales 3.Prices 4.End of Day 5.Exit')
  choice = int(input('Enter choice:  '))
  if choice == 1:
      fill()
  elif choice == 2:
      sales()
  elif choice == 3:
      prices()
  elif choice == 4:
      end_of_day()
  elif choice == 5:
      quit = True
  else:
      print('Invalid Choice!')

