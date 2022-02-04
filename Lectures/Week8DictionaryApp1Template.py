taxpayers = {} #key: name  value: [income, married, tax]
#income = value[0]
#married = value[1]
#tax = value[2]


def compute_tax_rate(income, married):
    global taxpayers
    cutoff = 100000.0 if married else 70000.0

    return 0.15 if income > cutoff else 0.1

def process_line(input_str):
    global taxpayers
    inlist = input_str.split()
    name = inlist[0]
    income = float(inlist[1])
    #DIY validate income using a loop and a bool function, refer to video Version 1
    married = int(inlist[2])
    #DIY do similar validation for married

    tax_rate = compute_tax_rate(income, married)
    tax = income * tax_rate

    taxpayers[name] = [income, married, tax]

def submit():
    global taxpayers
    input_str = input('Enter name, income, marital status (1 for married, 0 if not): ')

    process_line(input_str)

    name = input_str.split()[0]
    income = taxpayers[name][1]
    tax = taxpayers[name][2]


    print(name, income, tax) #improve!

def load():
    with open('inputs.txt', 'r') as inflie: #infilie = open('inputs.txt', 'r')
        lines = inflie.readlines()

     #lines is a list of strings, each string a line

    for line in lines:
        process_line(line)

def save():
    # save contents of the dictionary to a text file, csv formatted
    #   open a file for writing
    #   loop through the dictionary
    #       write each taxpayer to the file

    with open('outfile.txt', 'w') as outfile:  #r read w write(overwrite) a append
        for key in taxpayers.keys():
            value = taxpayers[key]
            income = value[0]
            married = value[1]
            tax = value[2]
            out_line = f'{key:s},{income:2f},{married:d},{tax:.2f}\n'
            outfile.write(out_line) #(outline + '\n')
    
    print('All Data saved')

def summary():
    global taxpayers

    total_tax = 0.0
    taxpayercount = 0
    total_tax_married = 0.0
    married_count = 0
    for value in taxpayers.values():
        married = value[1]
        tax = value[2]
        total_tax += tax
        taxpayercount += 1
        
        if married:
            total_tax_married += tax
            married_count += 1
    
    if taxpayercount:
        average_tax = total_tax / taxpayercount
    else:
        average_tax = None

    if married_count:
        average_tax_married = total_tax_married / married_count
    else:
        average_tax_married = None

    if average_tax is not None:
        print(average_tax)
    else:
        print('No data')

    if average_tax_married is not None:
        print(average_tax_married)
    else:
        print('No data')

def clear_data():
    global taxpayers

    taxpayers.clear()

def reset():
    global taxpayers

    clear_data() # do not do taxpayers = []

def line():
    print('-' * 50)

def print_student_info(name):
    value = taxpayers[name]
    income = value[0]
    married = value[1]
    tax = value[2]
    print(f'|{name:<12s}|{income:12.2f}|{married:^9d}|{tax:12.2f}')

def display():
    global taxpayers
    #DIY: do this check in all functions that retrieve data drom the dictionary
    if not taxpayers:
        print('No data in database')
        return

    line()
    print(f'|{"Name":<12s}|{"Income":^12s}|{"Married":^9s}|{"Tax":^12s}')
    line()

    for key in taxpayers.keys():
        value = taxpayers[key]
        income = value[0]
        married = value[1]
        tax = value[2]
        print(f'|{key:<12s}|{income:12.2f}|{married:^9d}|{tax:12.2f}')
    line()

def search():
    global taxpayers

    if not taxpayers:
        print('No data to search')
        return

    key = input('Enter the name to search for: ')
    if key in taxpayers.keys():
        value = taxpayers[key]
        income = value[0]
        married = value[1]
        tax = value[2]
        print(f'|{key:<12s}|{income:12.2f}|{married:^9d}|{tax:12.2f}')
    else:
        print('No such taxpayer in the database..')
#main
quit = False
while not quit:
   print('1.Submit 2.Load 3.Summary 4.Save 5.Display 6.Search 7.Reset 8.Exit')
   choice = int(input('Enter choice:  '))
   if choice == 1:
       submit()
   elif choice == 2:
       load()
   elif choice == 3:
       summary()
   elif choice == 4:
       save()
       
   elif choice == 5:
       display()
   elif choice == 6:
       search()
   elif choice == 7: 
       reset()    
       print('Data cleared. Ready for new series...')
   elif choice == 8:
       quit = True   
       clear_data()
   else:
       print('Invalid Choice!')

#CODE TO Deal with FILE LOCATION ISSUES
#ENSURE input file is in same folder as .py file.
""" To Make your code work with text files in same folder as the .py files regardless of environment and editor used:
use this code. (the import statement goes as the first line in your .py file, the rest goes where you do the file open and read, and replace the .txt with your filename
this assumes your input file is in same folder as .py file

import os.path   #first line up top in .py

filepath = os.path.dirname(__file__)
filename = os.path.join(filepath, 'test.txt')  # replace test.txt with what you need

with open(filename, 'r') etc..
"""


