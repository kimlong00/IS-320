#5

#globals
grade_a_count = 0
grade_b_count = 0
grade_c_count = 0
grade_d_count = 0
grade_f_count = 0
perfect_score_count = 0
total_score = 0

def update_gradecounts(score):
    global grade_a_count, grade_b_count, grade_c_count, grade_d_count, grade_f_count, perfect_score_count, total_score
    total_score += score
    if score == 100:
        perfect_score_count += 1

    if score >= 90:
        grade_a_count += 1
    elif score >= 80:
        grade_b_count += 1
    elif score >= 70:
        grade_c_count += 1
    elif score >= 60:
        grade_d_count += 1
    else:
        grade_f_count += 1

def compute_average_score():
    avg_score = total_score / (grade_a_count + grade_b_count + grade_c_count + grade_d_count + grade_f_count)

    return avg_score

def submit():
    #inputs
    score = int(input('Enter score: '))

    #computations
    update_gradecounts(score)

def summary():
    average_score = compute_average_score()
    print(f'\nSummary of Letter Grades:\n\nClass Average : {average_score:.2f}')
    print(f'A: {grade_a_count:d}\nB: {grade_b_count:d}\nC: {grade_c_count:d}\nD: {grade_d_count:d}\nF: {grade_f_count:d}')
    print(f'Perfect Scores : {perfect_score_count:d}')

#main
for x in range(10):
    submit()

summary()