"""HW5 Problem 2 Developed by Kimlong Nguyen 11.14.21

App takes in a name, score, and grade basis and computes a corresponding grade.
Under grade basis, if score is above 80, grade is an A, otherwise a B.
If not under grade basis, score of 40 and above is a pass, otherwise fail.

Inputs: Name (str) Score (int) Grade Basis (int)

Outputs: All listed inputs, Score (int) Grade (str)
"""

#globals
namelist = [] # contains all the inputed names
scorelist = [] # contains all the inputed scores
statuslist = [] # contains all grade status either graded or pass/fail
gradelist = [] # contains all grades scores such as A, B, Pass

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
    global namelist, scorelist, statuslist, gradelist

    grade = 'B'
    if score > 80:
        grade = 'A'

    gradelist.append(grade)
    
    return grade

def compute_passfail(score):
    """Determines whether the inputed score is a pass/fail
    Passing score is is 40 or above, otherwise a fail
    
    Paramters:
        score (int)
    Returns
        grade (string)
    """
    global namelist, scorelist, statuslist, gradelist

    grade = 'Fail'
    if score >= 40:
        grade = 'Pass'
    
    gradelist.append(grade)
    
    return grade

def compute_average_score():
    """Computes Average score, if there are values
    
    Parameters:
        None
    Returns:
        average score (float) input count (int)
    """

    global namelist, scorelist, statuslist, gradelist

    total_score = 0.0
    input_count = 0
    
    for score in scorelist:
        total_score += score
        input_count += 1

    if input_count > 0:
        avg = total_score / input_count
    else:
        avg = None

    return avg, input_count,

def clear_list():
    """Clears all the list in the global variables
    
    Paramters:
        None
    Returns
        None
    """

    global namelist, scorelist, statuslist, gradelist

    namelist.clear()
    scorelist.clear()
    statuslist.clear()
    gradelist.clear()


def submit():
    global namelist, scorelist, statuslist, gradelist
    
    name = str(input('Enter a name: '))
    
    if not name.isalpha():
        print('Please enter a valid name')
        return

    score = int(input('Enter a score: '))

    if not is_valid_score(score):
        print('Please enter a score between 0 and 100')
        return

    graded = int(input('Enter 1 for grade basis, 0 for pass/fail: '))
    if not is_valid_graded(graded):
        print('Invalid input, Please enter 1(yes) or 0(no)')
        return

    #computations
    if graded:
        grade = compute_grade(score)
        status = 'Graded'
        statuslist.append(status)
    else:
        grade = compute_passfail(score)
        status = 'PassFail'
        statuslist.append(status)

    #updates
    namelist.append(name)
    scorelist.append(score)

    #outputs
    print(f'Name: {name:s}  Score: {score:d}    Status: {status:s}')
    print(f'Grade: {grade:s}')

def summary():
    global namelist, scorelist, statuslist, gradelist

    average_score, number_of_inputs = compute_average_score()

    if average_score is not None:
        print(f'Average Score : {average_score:.2f} | Number of Inputs: {number_of_inputs:d}')
    else:
        print('No Data')

def reset():
    global namelist, scorelist, statuslist, gradelist

    clear_list()

def line():
    print('-' * 44)

def display():
    global namelist, scorelist, statuslist, gradelist

    if not namelist:
        print('No data to display!')
        return

    line()
    print(f'|{"Name":^15s}|{"Score":^7s}|{"Status":^10s}|{"Grade":^7s}|')
    line()

    for name, score, status, grade, in zip(namelist, scorelist, statuslist, gradelist):
        print(f'|{name:^15s}|{score:^7d}|{status:^10s}|{grade:^7s}|')

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