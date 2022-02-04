"""Kimlong Nguyen Question 1"""

#globals
num_taxpayers = 0 # counts the number of all taxpayers
student_taxpayers = 0 # counts the numbers of student taxpayers 
total_tax_students = 0.0 # counts the total ammount of tax paid across students
tax_list = [] # list to store all tax values from each input
single_students = 0 # counts the number of single students

#functions
def count_regular_exemptions(married, student, num_jobs, income ):
    global num_taxpayers, student_taxpayers, total_tax_students, tax_list, single_students

    num_exemptions = 1
    if not num_jobs:
        num_exemptions += 1
    elif num_jobs == 1:
        if married:
            num_exemptions += 1
        elif student:
            num_exemptions += 1
            single_students += 1
    elif income < 1500:
        num_exemptions += 1
    
    return num_exemptions

def count_child_exemptions(income, children):
    global num_taxpayers, student_taxpayers, total_tax_students, tax_list, single_students

    if income < 70000:
        exemptions = children * 4
    else:
        exemptions = children // 2
    
    return exemptions

def compute_taxable_income(income, regular_exemptions, child_exemptions):
    global num_taxpayers, student_taxpayers, total_tax_students, tax_list, single_students

    exemption_amount = child_exemptions * 1000.0
    exemption_amount += regular_exemptions * 2000.0
    taxable_income = income - exemption_amount

    return taxable_income

def compute_tax_rate(married, taxable_income):
    global num_taxpayers, student_taxpayers, total_tax_students, tax_list, single_students

    if (married and taxable_income <= 78000) or (not married and taxable_income <= 38000):
        tax_rate = 0.1
    else:
        tax_rate = 0.15
    
    return tax_rate

def compute_deduction(student, income):
    global num_taxpayers, student_taxpayers, total_tax_students, tax_list, single_students

    deduction = 0.0   
    if student:
        student_taxpayers += 1
        if income < 57000:
            deduction = 3000.0
        elif income < 80000:
            deduction = 2000.0

    return deduction

def compute_tax(taxable_income, tax_rate, deduction, student):
    global num_taxpayers, student_taxpayers, total_tax_students, tax_list, single_students

    tax = taxable_income * tax_rate - deduction
    if tax < 0:
        tax = 0.0
    
    if student:
        total_tax_students += tax

    return tax

def compute_average_tax():
    global num_taxpayers, student_taxpayers, total_tax_students, tax_list, single_students

    if student_taxpayers > 0:
        average_tax = total_tax_students / student_taxpayers
    else:
        average_tax = None

    return average_tax

def process_inputs(num_jobs, income, num_children, married, student):
    global num_taxpayers, student_taxpayers, total_tax_students, tax_list, single_students
    
    regular_exemptions = count_regular_exemptions(married, student, num_jobs, income)
    child_exemptions = count_child_exemptions(income, num_children)
    taxable_income = compute_taxable_income(income, regular_exemptions, child_exemptions)
    tax_rate = compute_tax_rate(married, taxable_income)
    deduction = compute_deduction(student, income)
    tax = compute_tax(taxable_income, tax_rate, deduction, student)

    #updates
    num_taxpayers += 1
    tax_list.append(tax)

    return tax

def submit():
    global num_taxpayers, student_taxpayers, total_tax_students, tax_list, single_students
    #inputs
    num_jobs = int(input('Enter the number of jobs: '))

    if num_jobs < 0:
        print('Invalid Input! Please enter a positive value\n')
        return

    income = float(input('Enter income: '))
    num_children = int(input('Enter the number of children: '))
    
    if num_children < 0:
        print('Invalid Input! Please enter a positive value\n')
        return
    
    married = int(input('Are you married? (1)=yes (2)=no: '))
    student = int(input('Are you a student? (1)=yes (2)=no: '))
    
    if student != 0 and student != 1:
        print('Invalid Input! Please enter (1)=yes (2)=no\n')
        return

    #computations
    tax = process_inputs(num_jobs, income, num_children, married, student)

    #outputs
    print(f'Tax owe: ${tax:.2f}\n')

def summary():
    global num_taxpayers, student_taxpayers, total_tax_students, tax_list, single_students

    average_tax = compute_average_tax()
    married_students = student_taxpayers - single_students
    non_student_taxpayers = num_taxpayers - student_taxpayers
    print('\nSummary Output:')

    if num_taxpayers:
        if average_tax is not None:
            print(f'Number of Taxpayers: {num_taxpayers:d}, Average tax for students: ${average_tax:.2f}')
        else:
            print('No students taxpayers entered')

        print(f'Number of single students: {single_students:d}')
        print(f'Number of married students: {married_students:d}')
        print(f'Number of non-student taxpayers: {non_student_taxpayers:d}\n')
    else:
        print('No taxpayers inputed!')
    
def reset():
    global num_taxpayers, student_taxpayers, total_tax_students, tax_list, single_students

    num_taxpayers = 0
    student_taxpayers = 0
    total_tax_students = 0.0
    tax_list.clear()

def display():
    global num_taxpayers, student_taxpayers, total_tax_students, tax_list, single_students
    
    if tax_list:
        print('-----------------')
        print('-------Tax-------')
        print('-----------------')
        for tax in tax_list:
            print(f'${tax:.2f}')
        print('-----------------')
    else:
        print('No taxes to display!')        

#main
quit = False
while not quit:
   print('1.Submit 2.Summary 3.Reset 4.Display 5.Exit')
   choice = int(input('Enter choice:  '))
   if choice == 1:
       submit()
   elif choice == 2:
       summary()
   elif choice == 3:
       reset()
   elif choice == 4:
       display() 
   elif choice == 5:
       quit = True
   else:
       print('Invalid Choice!')