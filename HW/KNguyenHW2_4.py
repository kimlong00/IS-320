"""HW 2 Problem 4 developed by Kimlong Nguyen 10.14.21

This app computes the total score of two homeworks tests
and scales it proportionally to 60 and 40 to create a total score.
The total score is used to determine the letter grade.
In the condition where the student grade is a B,
the grade can be an A if either of the test score is 30.
Input (from user): Name (string), Homework 1 and 2 scores (float), Test 1 and 2 scores (float)
Output: Name (string), Homework 1 and 2 scores (float), Test 1 and 2 scores(float) 
"""

#inputs
student_name = input('What is your name?:  ')
hw_score1 = float(input('Enter your 1st homework score:  '))
hw_score2 = float(input('Enter your 2nd homework score:  '))
test_score1 = float(input('Enter your 1st test score: '))
test_score2 = float(input('Enter your 2nd test score: '))

#initializations
hw_score_max = 50.0
test_score_max = 30.0
hw_scaled = 60.0
test_scaled = 40.0

#computations
#Function takes two scores and a max possible score to calculate the average score of the two inputs
def average_score(score1, score2, max_score):
    score1_percent = score1 / max_score
    score2_percent = score2 / max_score
    score_average = (score1_percent + score2_percent) / 2
    return score_average

hw_average_percent = average_score(hw_score1, hw_score2, hw_score_max)
test_average_percent = average_score(test_score1, test_score2, test_score_max)
scaled_total_score = hw_average_percent * hw_scaled + test_average_percent * test_scaled

if scaled_total_score > 90:
    grade = 'A'
elif scaled_total_score > 80:
    if test_score1 == 30 or test_score2 == 30:
        grade = 'A'
    else:
        grade = 'B'
elif scaled_total_score >= 60:
    grade = 'C'
else:
    grade = 'D'

#outputs
print(f'\nName: {student_name:s} \nHomework 1: {hw_score1:.2f}/50 \nHomework 2: {hw_score2:.2f}/50 \n')
print(f'Test 1: {test_score1:.2f}/30 \nTest 1: {test_score2:.2f}/30')
print(f'Scaled Total Score: {scaled_total_score:.2f}/100 \n\nGrade: {grade:s}')
