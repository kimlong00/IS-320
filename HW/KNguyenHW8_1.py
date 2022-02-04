"""HW8 Problem 1 Developed by Kimlong Nguyen 12.12.21

App takes in a name, score, and grade basis and computes a corresponding grade.
Under grade basis, if score is above 80, grade is an A, otherwise a B.
If not under grade basis, score of 40 and above is a pass, otherwise fail.
App allows user to search a student, diplay all students info and summarize results.

Inputs: Name (str) Score (int) Grade Basis (int)

Outputs: All listed inputs, Score (int) Grade (str) numbers of sutdents, grades, 100s and 0s (int)
"""

import sqlite3

#globals
connection = sqlite3.connect('grades.db')
cur = connection.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS students
(name text,
score integer,
status integer,
grade text
)
''')

#functions
def is_valid_score(score):
    """Boolean function to check if inputed score is valid or not. Between 0-100 is valid
    Parameter:
        score (int)
    Returns
        Boolean
    """

    return score >= 0 and score <= 100

def is_valid_graded(graded):
    """Boolean function to check if graded input is valid or not (1 or 0)
    Parameter: 
        graded (int)
    Returns
        Boolean
    """
    return graded == 1 or graded == 0

def compute_grade(score):
    """Computes a letter grade when inputed a number between 0-100
    If score is above 80, grade is an A, otherwise a B.
    
    Parameters:
        score (int)
    Returns
        grade (string)
    """
    
    return 'A' if score > 80 else 'B'

def compute_passfail(score):
    """Determines whether the inputed score is a pass/fail
    Passing score is is 40 or above, otherwise a fail
    
    Paramters:
        score (int)
    Returns
        grade (string)
    """
    
    return 'Pass' if score >= 40 else 'Fail'

def load():

    with open('G:\My Drive\IS 320\HW\hwscore.txt', 'r') as infile:
        lines = infile.readlines()
    
    for line in lines:
        process_line(line, ',')
    
    number_of_students = len(lines)
    print(number_of_students, 'students loaded')

def process_line(input_str, sep = None):
    inlist = input_str.split(sep)
    name = inlist[0]
    score = int(inlist[1])
    grade = int(inlist[2])
    
    process_inputs(name, score, grade)

def process_inputs(name, score, graded):

    if graded:
        grade = compute_grade(score)
        status = 'Graded'
    else:
        grade = compute_passfail(score)
        status = 'PassFail'

    cur.execute('INSERT into students values (?,?,?,?)', (name,score,status,grade))
    connection.commit()

    return status, grade

def submit():

    input_str = input('Enter name, score, and grade type (1 for grade basis, 0 for pass/fail): ')
    input_list = input_str.split()
    name = input_list[0]    
    
    while not name.isalpha():
        print('Please enter a valid name')
        name = str(input('Enter a name: '))
    
        if name.isalpha():
            break
    
    score = int(input_list[1])
    
    while not is_valid_score(score):
        print('Invalid score! Please enter a score between 0 and 100')
        score = int(input('Enter a score: '))

        if is_valid_score(score):
            break
    
    graded = int(input_list[2])

    while not is_valid_graded(graded):
        print('Invalid input, Please enter 1(yes) or 0(no)')
        graded = int(input('Enter 1 for grade basis, 0 for pass/fail: '))
        if is_valid_graded(graded):
            break

    status, grade = process_inputs(name, score, graded)

    #outputs
    display_header()
    print(f'|{name:^15s}|{score:^7d}|{status:^10s}|{grade:>7s}|')
    line()

def divide(numerator, denominator):
    """Given two inputs, divide if possible, else none.
    
    Parameters:
        numerator (int), denominator (int)
    Returns:
        average score (float)
    """
    
    return numerator / denominator if denominator else None

def compute_averages():

    total_score_graded = 0.0
    total_score = 0.0
    student_count = 0
    grade_b_count = 0
    grade_a_count = 0
    score_0_count = 0
    score_100_count = 0
    
    for row in cur.execute('select * from students'):
        score = row[1]
        grade = row[3]
        total_score += score
        student_count += 1

        if grade == 'A':
            grade_a_count += 1
            total_score_graded += score
        elif grade == 'B':
            grade_b_count += 1
            total_score_graded += score
        
        if not score:
            score_0_count += 1
        elif score == 100:
            score_100_count += 1
    
    grade_count = grade_a_count + grade_b_count
    total_average = divide(total_score, student_count)
    graded_average = divide(total_score_graded, grade_count)
    
    return total_average, graded_average, student_count, grade_b_count, grade_a_count, score_0_count, score_100_count

def summary():
    cur.execute('select count(*) from students')
    row_count = cur.fetchone()[0]
    
    if not row_count:
        print('No data Available')
        return
    
    total_average, graded_average, student_count, grade_b_count, grade_a_count, score_0_count, score_100_count = compute_averages()

    line(32)
    print(f'|{"Average score":<22s}|{total_average:^7.2f}|')
    line(32)

    if graded_average is None:
        print('|No Data to calculate graded average|')
    else:
        print(f'|{"Average graded score":<22s}|{graded_average:^7.2f}|')

    line(74)
    print(f'|{"Number of Students":^20s}|{"A grades":^12s}|{"B grades":^12s}|{"0s scores":^11s}|{"100s scores":^13s}|')
    line(74)
    print(f'|{student_count:^20d}|{grade_a_count:^12d}|{grade_b_count:^12d}|{score_0_count:^11d}|{score_100_count:^13d}|')
    line(74)


def clear_data():
    cur.execute('delete from students')
    connection.commit()

def reset():
    clear_data()
    print('Database Reset! Ready for new inputs.')

def line(multiplier = 44):
    print('-' * multiplier)

def display_header():
    """Diplay header concisting of name, score, status and grade.
    
    Parameters:
        None
    Returns:
        None
    Display
        Name, score, status, status, grade (str)"""
    line()
    print(f'|{"Name":^15s}|{"Score":^7s}|{"Status":^10s}|{"Grade":^7s}|')
    line()

def convert_to_csv(student_list):
    """Given a list, convert and return a string list in csv format
    
    Parameters:
        list
    Return
        score, grade_status, grade (str)"""

    global students_grade

    score = student_list[0]
    grade_status = student_list[1]
    grade = student_list[2]
    
    return f'{score:d},{grade_status:s},{grade:s}'

def print_student_info(row):
    name = row[0]
    score = row[1]
    status = row[2]
    grade = row[3]
    print(f'|{name:^15s}|{score:^7d}|{status:^10s}|{grade:^7s}|')

def display():
    cur.execute('select count(*) from students')
    row_count = cur.fetchone()[0]
    if row_count:
        display_header()
        for row in cur.execute('select * from students'):
            print_student_info(row)
        line()
    else:
        print('No data to display')
        
def search():
    cur.execute('select count(*) from students')
    row_count = cur.fetchone()[0]
    if row_count:
        while True:
            name = input('Enter the name to search for: ')

            if name.isalpha():
                break

            print('Please enter a valid name')
        
        count = 0
        display_header()
        for row in cur.execute('select * from students where name like :key', {'key':name}):
            print_student_info(row)
            count += 1

        print(count, 'records found')
    else:
        print('No data to search')

#main
quit = False
while not quit:
   print('1.Submit 2.Load 3.Summary 4.Display 5.Search 6.Reset 7.Exit')
   choice = int(input('Enter choice:  '))
   if choice == 1:
       submit()
   elif choice == 2:
       load()
   elif choice == 3:
       summary()      
   elif choice == 4:
       display()
   elif choice == 5:
       search()
   elif choice == 6: 
       reset()
   elif choice == 7:
       quit = True
   else:
       print('Invalid Choice!')
    
connection.commit()
connection.close()