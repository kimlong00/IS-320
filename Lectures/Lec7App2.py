"""Lecture 7 App 2.  Nested If, Function Design, Bool Input."""


"""Problem Spec:
A score (int) may be on grade basis, or pass fail basis.
No other possibility exists.
Graded:  A > 80, B Otherwise.
PassFail: Pass >= 40 Fail Otherwise.

inputs: score int, grade_basis str  ('y' 'n')
output: grade. str.
"""

"""Our sequence will be to:
1. code without functions
2. extract the computation from main, and package it as a function (encapsulation)
3. implementing an alternate design with two functions for A/B  Pass/Fail
4. exploring alternate ways of reading the input
"""

#functions
def compute_grade(sc, is_graded):
    """computes grade. 
    
    input: score (int), grade basis (str)  output: grade (str)"""

    if is_graded == 'y':
        #A or B
        if sc > 80:
            grade = 'A'
        else:
            grade = 'B'
    else:
        #Pass or Fail
        if sc >= 40:
            grade = 'P'
        else:
            grade = 'F'

    return grade


#main
#input
score = int(input('Score? >>'))
grade_basis = input('Enter y for graded, n for pass/fail: >>')


#computations

grade = compute_grade(score, grade_basis)  # sc = score  is_graded = grade_basis

#output
print(grade)
