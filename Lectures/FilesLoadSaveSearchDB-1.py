import os.path
import sqlite3

#globals
connection = sqlite3.connect('tax.db') 
cur = connection.cursor() 
cur.execute('''CREATE TABLE IF NOT EXISTS taxpayers
(name  text,
income real,
married integer,
tax real
)
''')




#functions
def find_rate(income):
    return 0.1 if income < 100000.0 else 0.15


def submit():
    

    line = input('Enter name, income  and married (1 or 0)>>')
    in_list = line.split()
    name = in_list[0]
    
    income = float(in_list[1])
    #validate income here, using loop. Use Version 1 from Validation video.

    married = int(in_list[2])
    #validate married here, using loop.Use Version 1 from Validation video.

    tax_rate = find_rate(income)
    tax = income * tax_rate

    
    cur.execute('INSERT into taxpayers values (?,?,?,?)',(name,income,married,tax))
    connection.commit()


    print(name,income, tax)


def summary():
    

    #average income, average tax
    total_income = 0.0
    total_tax = 0.0
    count = 0
    married_count = 0
    married_total_tax = 0.0

    for row in cur.execute('select * from taxpayers'):
            
        
        income = row[1]
        married = row[2]
        tax = row[3]
        total_income = total_income + income  # total_income + value[0]
        total_tax = total_tax + tax  #total_tax + value[1]
        count = count + 1
        if married:
            married_count = married_count + 1
            married_total_tax = married_total_tax + tax

    if count > 0:
        average_income = total_income / count
        average_tax = total_tax / count
    else:
        average_income = average_tax = None

    if average_income is not None:
        print(average_income, average_tax, count)
    else:
        print('No data to compute averages with...')


    


def reset():
    
    cur.execute('delete from taxpayers')
    connection.commit()
    


def display():
    

    cur.execute('select count(*) from taxpayers')
    row_count = cur.fetchone()[0]   # (5,) -> 5
    #print(count)
    if row_count:
        #caption
        for row in cur.execute('select * from taxpayers'):
            
            name = row[0]
            income = row[1]
            married = row[2]
            tax = row[3]
            print(f'|{name:<12s}|{income:12.2f}|{married:5d}|{tax:12.2f}|')

    else:
        print('No data....')
    

def search():
    
    name = input('Enter name to search for: >>')
    count = 0
    for row in cur.execute('select * from taxpayers where name like :key', {'key':name}):
    
        name = row[0]
        income = row[1]
        married = row[2]
        tax = row[3]
        print(f'|{name:<12s}|{income:12.2f}|{married:5d}|{tax:12.2f}|')
        count += 1
    
    print(count, 'records found')

  

def load():
   

    filepath = os.path.dirname(__file__)
    filename = os.path.join(filepath, 'in.txt')  # replace test.txt with what you need

    #open a text file, that you already made,
    with open(filename, 'r') as inputfile:
        lines = inputfile.readlines()     #read its contents as lines into a list.
    
    for line in lines:
        in_list = line.strip('\n').split(',')
        name = in_list[0]
        income = float(in_list[1])
        married = int(in_list[2])
        tax_rate = find_rate(income)
        tax = income * tax_rate
        
        cur.execute('INSERT into taxpayers values (?,?,?,?)', (name,income,married,tax))

    connection.commit()



# def save():
#     global taxpayers

#     #write to a new file, from the dictionary  
#     with open('outfile.txt', 'w') as outfile:
#         for name in taxpayers.keys():
#             value = taxpayers[name]
#             income = value[0]
#             married = value[1]
#             tax = value[2]
#             out_line = f'{name:s},{income:.2f},{married:d},{tax:.2f}\n'
#             outfile.write(out_line)

#     print('All data saved...')




    

#main
quit = False
while not quit:
   print('1.Submit 2.Load 3.Summary 4.Save 5.Display 6.Search 7. Reset 8. Exit')
   choice = int(input('Enter choice:  '))
   if choice == 1:
       submit()
   elif choice == 2:
       load()
   elif choice == 3:
       summary()
   elif choice == 4:
       pass
       #save()
       
   elif choice == 5:
       display()
   elif choice == 6:
       search()
   elif choice == 7: 
       reset()    
       print('Data cleared. Ready for new series...')
   elif choice == 8:
       quit = True   
      
   else:
       print('Invalid Choice!')

connection.commit()
connection.close()




""" To Make your code work with text files in same folder as the .py files regardless of environment and editor used:
use this code. (the import statement goes as the first line in your .py file, the rest goes where you do the file open and read, and replace the .txt with your filename
this assumes your input file is in same folder as .py file

import os.path   #first line up top in .py

filepath = os.path.dirname(__file__)
filename = os.path.join(filepath, 'test.txt')  # replace test.txt with what you need

with open(filename, 'r') etc..
"""