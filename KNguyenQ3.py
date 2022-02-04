"""Kimlong Nguyen Question 3"""

#globals
perfect_scores = 0 # counts the number of perfect scores
total_score_basis = 0.0 # counts the total number of score for grade basis inputs
grade_a = 0 # counts the number of A grades
grade_b = 0 # counts the number of B grades
pass_grade = 0 # counts the number of pass grades on no grade basis
fail_grade = 0 # counts the number of fail grade on no grade basis
score_list = [] # a list to store all inputed scores

#functions
def update_grade_counts(grade_basis, score):
    global perfect_scores, total_score_basis, grade_a, grade_b, pass_grade, fail_grade, score_list

    if grade_basis:
        total_score_basis += score
        if score > 80:
            grade_a += 1
        else:
            grade_b += 1
    else:
        if score >= 40:
            pass_grade += 1
        else:
            fail_grade += 1
    
    if score == 100:
        perfect_scores += 1
    
    score_list.append(score)

def compute_average_score():
    global perfect_scores, total_score_basis, grade_a, grade_b, pass_grade, fail_grade, score_list

    if grade_a + grade_b > 0:
        average_score = total_score_basis / (grade_a + grade_b)
    else:
        average_score = None

    return average_score

def submit():
    global perfect_scores, total_score_basis, grade_a, grade_b, pass_grade, fail_grade, score_list
    #inputs
    score = float(input('Enter a score: '))
    
    if score < 0 or score > 100:
        print('Invalid input! Please enter a score between 0 and 100.')
        return

    grade_basis = int(input('Is score on grade basis? (1)=yes (2)=no: '))

    #computations
    update_grade_counts(grade_basis, score)

def summary():
    global perfect_scores, total_score_basis, grade_a, grade_b, pass_grade, fail_grade, score_list

    average_score_basis = compute_average_score()

    if average_score_basis is not None:
        print(f'\nSummary: Average (graded) score: {average_score_basis:.2f}')
        print(f'Grade A counts: {grade_a:d}\nGrade B counts: {grade_b:d}')
        print(f'Passed grades counts: {pass_grade:d}\nFailed grade counts: {fail_grade:d}\nPerfect score counts: {perfect_scores:d}\n')    
    elif pass_grade or fail_grade:
        print('No graded basis scores to calculate average score!')
        print(f'Grade A counts: {grade_a:d}\nGrade B counts: {grade_b:d}')
        print(f'Passed grades counts: {pass_grade:d}\nFailed grade counts: {fail_grade:d}\nPerfect score counts: {perfect_scores:d}\n')
    elif perfect_scores:
        print(f'Scores reset. No grades inputed! Total previous perfect scores: {perfect_scores:d}\n')
    else:        
        print('No grades inputed\n')

    average_score_basis

def reset():
    global perfect_scores, total_score_basis, grade_a, grade_b, pass_grade, fail_grade, score_list

    total_score_basis = 0.0
    grade_a = 0
    grade_b = 0
    pass_grade = 0
    fail_grade = 0
    score_list.clear()

def display():
    global perfect_scores, total_score_basis, grade_a, grade_b, pass_grade, fail_grade, score_list

    if score_list:
        print('----------------')
        print('-----Scores-----')
        print('----------------')
        for scores in score_list:
            print(f'{scores:.2f}')
        print('----------------')
    else:
        print('No scores to display!')

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