"""HW5 Problem 2 Developed by Kimlong Nguyen 11.14.21

App takes in a name, score, and grade basis and computes a corresponding grade.
Under grade basis, if score is above 80, grade is an A, otherwise a B.
If not under grade basis, score of 40 and above is a pass, otherwise fail.
App allows user to search a student, diplay all students info and summarize results.

Inputs: Name (str) Score (int) Grade Basis (int)

Outputs: All listed inputs, Score (int) Grade (str) numbers of sutdents, grades, 100s and 0s (int)
"""

#globals6
students_grades = {} #key: name value: [score, grade-status, grade]
#score = value[0]
#grade-status = value[1]
#grade = value[2]

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

def process_inputs(name, score, graded):
    """Process submit inputs, insert entries into dictionary
    
    Parameters:
        name (str), score (int), graded (int)
    Returns:
        None
    """
    global students_grade

    if graded:
        grade = compute_grade(score)
        status = 'Graded'
    else:
        grade = compute_passfail(score)
        status = 'PassFail'

    students_grades[name] = [score, status, grade]

def submit():
    global students_grade

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

    process_inputs(name, score, graded)
    status = students_grades[name][1]
    grade = students_grades[name][2]

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
    """Iterate through students_grades and count up the total scores graded or not, number of students,
    number of grade As and Bs, and number of 100s and 0s scores

    Parameters:
        None
    Returns:
        total score graded (float), total score (float), # student (int), # B grades (int), # A grades (int), # 0 scores (int), # 100s scores (int)
    """
    global students_grade

    total_score_graded = 0.0
    total_score = 0.0
    student_count = 0
    grade_b_count = 0
    grade_a_count = 0
    score_0_count = 0
    score_100_count = 0
    
    for value in students_grades.values():
        score = value[0]
        grade = value[2]
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
    global students_grade

    if not students_grades:
        print('No Data Available')
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


def reset():
    global students_grade

    students_grades.clear()
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

def print_student_info(name):
    """Given a name, function prints student's info
    
    Parameters:
        None
    Returns:
        None
    Display
        Student's name, score, status, grade (str)
    """
    global students_grade

    value = students_grades[name]
    score = value[0]
    status = value[1]
    grade = value[2]
    print(f'|{name:^15s}|{score:^7d}|{status:^10s}|{grade:>7s}|')

def display():
    global students_grade

    if not students_grades:
        print('No data in the database')
        return
    
    display_header()

    for name in students_grades.keys():
        print_student_info(name)
    line()
        
def search():
    """Prompt the user to enter a name. If possible, function will search and display the student's information.
    
    Parameters:
        None
    Returns:
        None
    User Inputs:
        name (str)
    Display
        Student's name, score, status, grade (str)

    """
    global students_grade

    if not students_grades:
        print('No data to search')
        return

    while True:
        name = input('Enter the name to search for: ')

        if name.isalpha():
            break

        print('Please enter a valid name')
    
    display_header()

    if name in students_grades.keys():
        print_student_info(name)
    else:
        print('No such student in the database.')
    line()

#main
quit = False
while not quit:
  print('1.Submit 2.Summary 3.Reset 4.Display 5.Search 6.Exit')
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
      search()
  elif choice == 6:
      quit = True
      students_grades.clear()  
  else:
      print('Invalid Choice!')