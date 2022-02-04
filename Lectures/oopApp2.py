"""
Taxpayer class:
    Attributes:
        name    income status tax_rate tax

    Methods: (functions, inside class)
    init : makes a new object. inputs: name, income status
    str: output as a string for use by print

    compute_tax_rate()
    compute_tax()
    display_line()

"""
#globals
taxpayerlist = []

#classes
class Taxpayer:
    count = 0 #track the number of taxpayers
    total_tax = 0.0
    married_count = 0

    def __init__(self, name, income, status):
        self.name = name
        self.income = income
        self.status = status
        self.tax_rate = self.compute_tax_rate()
        self.tax = self.compute_tax()

        #update Totals
        Taxpayer.count = Taxpayer.count + 1
        Taxpayer.total_tax += self.tax
        if self.status:
            Taxpayer.married_count += 1

    def __str__(self):
        return f'{self.name:s} {self.income:.2f} {self.tax:.2f}'
    
    def compute_tax_rate(self):
        cutoff = 1000.0 if self.status else 700.0

        return 0.2 if self.income > cutoff else 0.1

    def compute_tax(self):
        return self.income * self.tax_rate

    def display_line(self):
        return f'|{self.name:<10s}|{self.income:10.2f}|{self.tax:10.2f}|'

    def save_line(self):
        return f'{self.name:s},{self.income:.2f},{self.tax:.2f}'

    @classmethod
    def compute_average_tax(cls):
        if cls.count > 0:
            avg = cls.total_tax / cls.count
        else:
            avg = None
        
        return avg

    @classmethod
    def summary_string(cls):

        output_str = ''
        average_tax = cls.compute_average_tax()
        if average_tax is not None:
            output_str += f'{average_tax:.2f} {cls.count:d} {cls.married_count:d}'
        else:
            output_str += 'No data'

        return output_str
    
    @classmethod
    def reset_data(cls):
        cls.total_tax = 0.0
        cls.count = cls.married_count = 0

#functions
def convert_status(status):
    return 'Married' if status else 'Not Married'

def process_line(line, delimiter = None):
    inlist = line.split(delimiter)
    name = inlist[0]
    income = float(inlist[1])
    status = int(inlist[2])

    taxpayer = Taxpayer(name, income, status)
    taxpayerlist.append(taxpayer)

    return taxpayer

def submit():
    line = input('Name, income, status (1/0 for married or not): ')

    taxpayer = process_line(line)

    print(taxpayer)

def load():
    
    with open('G:\My Drive\IS 320\Lectures\oopApp2_inputs.txt', 'r') as infile:
        lines = infile.readlines()
    
    for line in lines:
        process_line(line)
    
    print('All data loaded...') #len(listname)
    

def display():
    global taxpayerlist

    if not taxpayerlist:
        print('No data to display!')
        return

    for taxpayer in taxpayerlist:
        print(taxpayer.display_line())

def summary():
    summary_report = Taxpayer.summary_string()
    print(summary_report)

def save():
    global taxpayerlist

    filename = input('Enter a name of file to save to: ')
    with open(filename, 'w') as outfile:
        for taxpayer in taxpayerlist:
            outfile.write(taxpayer.save_line() + '\n')

def reset():
    clear_data()
    Taxpayer.reset_data()

def clear_data():
    global taxpayerlist
    taxpayerlist.clear()

def search():
    if not taxpayerlist:
        print('No data to search for')
        return

    name = input('Enter name to search for: ')
    found = False

    #initialize a bool to track found or not.
    for taxpayer in taxpayerlist:
        print('checking..', taxpayer.name)
        if taxpayer.name == name:
            #flip the bool to indicate you found a match
            found = True
            print('found!')
            print(taxpayer) #print(taxpayer.search())
            break
    
    #run an if statement here to check the value of the bool.
    #   and report Not found! if appropriate
    if not found:
        print('Not found')


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