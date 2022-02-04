
#globals
single_taxpayer = 0 # count the number of single taxpayers
married_taxpayer = 0 # count the number of married taxpayers
student_taxpayer = 0 # count the number of student taxpayers

#functions

def calculate_exemption_count(married, num_job, student, income):
    global single_taxpayer, married_taxpayer, student_taxpayer
    exemption = 1
    if married:
        exemption += 1
        married_taxpayer += 1
    elif num_job == 1 and student:
        exemption += 1
    
    if num_job > 1 and income < 1500:
        exemption += 1

    return exemption

def calculate_child_exemption_count(married, income, kids):
    global single_taxpayer, married_taxpayer, student_taxpayer
    if (married and income < 100000) or (not married and income < 7000):
        exemption = kids * 4
    else:
        exemption = kids // 2

    return exemption

def compute_taxable_income(income, exemptions):
    global single_taxpayer, married_taxpayer, student_taxpayer
    exemption_ammount = exemptions * 2000
    if exemption_ammount > income:
        taxable_income = 0.0
    else:
        taxable_income = income - exemption_ammount

    return taxable_income

def compute_tax_rate(married, income):
    global single_taxpayer, married_taxpayer, student_taxpayer
    if (married and income <=19000) or (not married and income <= 9000):
        tax_rate = 0.1
    else:
        tax_rate = 0.12

    return tax_rate

def submit():
    global single_taxpayer, married_taxpayer, student_taxpayer
    #inputs
    num_jobs = 2
    income = 150000
    num_children = 11
    married = 1
    student = 0

    #computations
    exemption = calculate_exemption_count(married, num_jobs, student, income)
    child_exemption = calculate_child_exemption_count(married, income, num_children)
    total_exemptions = exemption + child_exemption
    taxable_income = compute_taxable_income(income, total_exemptions)
    tax_rate = compute_tax_rate(married, taxable_income)
    tax = taxable_income * tax_rate

    #outputs
    print(exemption, child_exemption, taxable_income, tax_rate, tax)

def summary():
    global single_taxpayer, married_taxpayer, student_taxpayer
    pass

def reset():
    global single_taxpayer, married_taxpayer, student_taxpayer
    pass

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