""" input: income outputs: tax, average tax
rate 10% below 100,000 else 15%.

income must be positive

new features:
repeated inputs from a menu
reset
validation of inputs
process_inputs function"""

#globals
total_tax = 0.0 #sum of all taxes, to compute average tax
input_count = 0 #count total number of inputs

#functions
def submit():
    global total_tax, input_count
    income = float(input('Enter Income: >> '))

    if income <= 0.0:
        print('Income must be above zero. Try again!')
        return

    #exemption_count = int(input('Enter number of exemptions: 0..4'))
    #if exemption_count < 0 or exemption_count > 4:
    # print('Number of exemptions must be in range 0..4')
    # return

    if income < 100000.0:
        tax_rate = 0.1
    else:
        tax_rate = 0.15

    tax = income * tax_rate

    total_tax += tax
    input_count += 1
    print(income, tax)

def summary():
    global total_tax, input_count
    
    average_tax = compute_average_tax()
    if average_tax is None:
        print('No inputs were entered')
    else:
        print(average_tax)

def compute_average_tax():
    global total_tax, input_count
    
    if input_count > 0:
        average = total_tax / input_count
    else:
        average = None
    
    return average

def reset():
    global total_tax, input_count

    total_tax = 0.0
    input_count = 0


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

# summary()
# submit()
# submit()
# summary()
# reset()
# summary()
# submit()
# summary()