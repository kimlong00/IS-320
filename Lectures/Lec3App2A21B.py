"""
input: score
output: grade
A: 90-100
B: 80-89
C: 0-79

display grade
"""

score = int(input('Enter score:     '))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'

print(f'score: {score:d} grade: {grade:s}')



#Notes
#if...
#elif...
#elif...
#else...