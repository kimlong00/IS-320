# 1 clear list function
# 2 checking for empty list in a different way

#globals
income_list = []
married_list = []
tax_list = []

#functions

def compute_tax_rate(income, married):
    
    return 0.1

def compute_tax(income, married):
    """Computes the tax.
    
    Parameters:
        income(float), married(int)
    Return:
        tax (float)
    """
    
    tax_rate = compute_tax_rate(income, married)

    return income * tax_rate

def is_valid_income(income):
    return income > 0.0

def is_valid_married(married):
    return married == 1 or married == 0

def submit():
    global income_list, married_list, tax_list

    #inputs
    income = float(input('Enter income >> '))
    if not is_valid_income(income):
        print('Please enter a positive value for income')
        return

    married = int(input('1 for married 0 if not >> '))
    if not is_valid_married(married):
        print('Please enter 1 for yes, 0 for no')
        return

    tax = compute_tax(income, married)
    income_list.append(income)
    married_list.append(married)
    tax_list.append(tax)
    print(income, married, tax)

def compute_average_income():
    """Computes Average Income, if there are values.
    
    Parameters:
        None
    
    """

    global income_list, married_list, tax_list

    total_income = 0.0
    input_count = 0
    for income in income_list:
        total_income += income
        input_count += 1
    
    if input_count > 0:
        avg = total_income / input_count
    else:
        avg = None

    return avg

def summary():
    average_income = compute_average_income()

    if average_income is not None:
        print(f'Average Income : {average_income:.2f}$')
    else:
        print('No data to compute average with..')

def clear_list():
    global income_list, married_list, tax_list
    
    income_list.clear()
    married_list.clear()
    tax_list.clear()


def line():
    print('-' * 42)

def display():
    global income_list, married_list, tax_list

    if not income_list: 
        print('No data to display!') #if the list is empty (strings and things, if empty, are false)
        return

    line()
    print(f'|{"Income":^14s}|{"Married":^11s}|{"Tax":^13s}|')
    line()

    for income, married, tax, in zip(income_list, married_list, tax_list): #each step extracts a 'tuple' (income, married)
        
        print(f'|{income:14.2f}|{married:^11d}|{tax:13.2f}|')

def reset():
    global income_list, married_list, tax_list

    clear_list()

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
        clear_list()
    else:
        print('Invalid Choice')