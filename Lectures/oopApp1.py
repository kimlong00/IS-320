#globals
taxpayerlist = [] # a list to hold taxpayer objects

#classes
class Taxpayer:
    def __init__(self,name, income):
        self.name = name
        self.income = income

    def __str__(self):
        return f'{self.name:s}\t{self.income:.2f}'

    def csv_string(self):
        return f'{self.name:s},{self.income:.2f}'

    def display_string(self):
        return f'|{self.name:^10s}|{self.income:12.2f}|'
#end class

#funcitons
def process_line(input_str):
    inlist = input_str.split()
    name = inlist[0]
    income = float(inlist[1])
    taxpayer = Taxpayer(name, income) # calling a built-in method __int__() makes and returns a taxpayer object.
    # a constructor     -init constructs an object. a constructor is called using the Class name. Taxpayer() Student()
    taxpayerlist.append(taxpayer)
    print(taxpayer)

def submit():
    input_str = input('Enter name and income >> ')
    process_line(input_str)

def load():
    with open('oopinputs.txt', 'r') as infile:
        lines = infile.readlines()
    
    for line in lines:
        process_line(line)
    
    print('All data loaded...')

def display():
    global taxpayerlist

    for taxpayer in taxpayerlist:
        print(taxpayer.display_string())

def summary():
    pass

def save():
    
    with open('oopoutputs.txt', 'w') as outfile: #alternatives is 'a' for append

        for taxpayer in taxpayerlist:
            outfile.write(taxpayer.csv_string() + '\n')

    print('All data saved')

def reset():
    clear_data()

def clear_data():
    global taxpayerlist
    taxpayerlist.clear()

def search():
    pass


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
