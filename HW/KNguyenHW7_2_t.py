#globals
student_list = [] # a list to hold student objects
need_save = True # keep track of whether the app needs to save or not
save_name = None # keep track of the output file name

#classes
class Student:
    count = 0 # track the number of students
    grade_count = 0 # tracks the numver of scores that are on a grade basis
    total_score = 0 # track the total socre of all students
    total_graded_score = 0 # tracks the total score that are on a grade basis
    total_a = 0 # tracks the total number of As grades
    total_100 = 0 # tracks the total number of perfect scores: 100

    def __init__(self, name, score, status, division):
        self.name = name
        self.score = score
        self.status = status
        self.division = division
        self.grade = self.compute_grade()

        Student.count += 1
        Student.total_score += self.score
        
        if score == 100:
            Student.total_100 += 1

    def compute_grade(self):
        if self.status == 'Graded':
            Student.grade_count += 1
            Student.total_graded_score += self.score
            if self.division == 'Upper':
                if self.score >= 90:
                    grade = 'A'
                    Student.total_a += 1
                else:
                    grade = 'B'
            else:
                if self.score >= 80:
                    grade = 'A'
                    Student.total_a += 1
                else:
                    grade = 'B'
        else:
            grade = 'Pass' if self.score >= 40 else 'Fail'
        
        return grade

 
    def __str__(self):
        return f'Name: {self.name:s}|Score: {self.score:d}|Status: {self.status:s}|Division: {self.division:s}|Grade: {self.grade:s}'
    
    def display(self):
        return f'|{self.name:^15s}|{self.score:^10d}|{self.status:^10s}|{self.division:^9s}|{self.grade:^10s}|'
    
    def search(self):
        return f'|{self.name:^15s}|{self.score:^10d}|{self.status:^10s}|{self.division:^9s}|{self.grade:^10s}|'
    
    def info_csv(self):
        return f'{self.name:s},{self.score:d},{self.status:s},{self.division:s},{self.grade:s}'


    @classmethod
    def compute_average_score(cls):
        if cls.count > 0:
            avg = cls.total_score / cls.count
        else:
            avg = None
        
        return avg
    
    @classmethod
    def compute_average_graded_score(cls):
        if cls.grade_count > 0:
            avg = cls.total_graded_score / cls.grade_count
        else:
            avg = None
        
        return avg
    
    @classmethod
    def summary_string(cls):

        average_score = cls.compute_average_score()
        average_graded_score = cls.compute_average_graded_score()
        output_str = f'|{"Average Score":^15s}|{"Number of students":^20s}|{"Average score (grade basis)":^30s}|{"Number of As":^15s}|{"Number of 100s":^16s}|\n'

        if average_score is None:
            return None
        
        if not average_graded_score:
            output_str += f'|{average_score:^15.2f}|{cls.count:^20d}|{"No graded score to compute!":^30s}|{cls.total_a:^15d}|{cls.total_100:^16d}|'
        else:
            output_str += f'|{average_score:^15.2f}|{cls.count:^20d}|{average_graded_score:^30.2f}|{cls.total_a:^15d}|{cls.total_100:^16d}|'

        return output_str

    @staticmethod
    def line(multiplier = 60):
        return '-' * multiplier

#end class

def line(multiplier = 49):
    print('-' * multiplier)

def convert_division(division):
    return 'Upper' if division else 'Lower'

def convert_to_status(graded):
    return 'Graded' if graded else 'PassFail'

def is_valid_score(score):
    return score >= 0 and score <= 100

def is_valid_graded(graded):
    return graded == 1 or graded == 0

def is_valid_division(division):
    return division == 1 or division == 0

def process_line(input_str, sep = None):
    global student_list, need_save, save_name
    inlist = input_str.split(sep)
    name = inlist[0]
    score = int(inlist[1])
    raw_status = int(inlist[2])
    raw_division = int(inlist[3])

    while not name.isalpha():
        print('Please enter a valid name')
        name = input('Enter a name: ')

        if name.isalpha():
            break
    
    while not is_valid_score(score):
        print('Invalid score! Please enter a score between 0 and 100')
        score = int(input('Enter a score: '))

        if is_valid_score(score):
            break

    while not is_valid_graded(raw_status):
        print('Invalid input! Enter 1 or 0')
        raw_status = int(input('Enter 1 for grade basis, 0 for pass/fail: '))
        if is_valid_graded(raw_status):
            break
    
    while not is_valid_division(raw_division):
        print('Invalid input, Please enter 1 or 0')
        raw_division = int(input('Enter a division type 1 for upper, 0 for lower: '))
        
        if is_valid_division(raw_division):
            break
         
    status = convert_to_status(raw_status)
    division = convert_division(raw_division)
    student = Student(name, score, status, division)
    student_list.append(student)

    return student

def submit():
    global student_list, need_save, save_name
    input_str = input('Enter name, score, grade type (1 for grade basis, 0 for pass/fail), division type (1 for upper, 0 for lower): ')

    student = process_line(input_str, None)
    need_save = True
    print(student)
    

def load():
    global student_list, need_save, save_name
    
    with open('G:\My Drive\IS 320\HW\HW7_2inputs.csv', 'r') as infile:
        lines = infile.readlines()
    
    for line in lines:
        process_line(line,',')
    
    need_save = True
    print('All data loaded')

def summary():
    global student_list, need_save, save_name

    if not student_list:
        print('No Data Available')
        return
    
    print(Student.line(102))
    print(Student.summary_string())
    print(Student.line(102))

def display():
    global student_list, need_save, save_name

    if not student_list:
        print('No data to display!')

    print(Student.line())

    for students in student_list:
       print(students.display())
    
    print(Student.line())

def save():
    global student_list, need_save, save_name

    if not need_save:
        print('Data have already been saved')
        return

    if save_name is None:
        save_name = input('Enter the name of the file to save to: ')

    with open(save_name, 'w') as outfile:

        for students in student_list:
            outfile.write(students.info_csv() + '\n')
    
    print(f'Data saved to: "{save_name:s}"')
    
    need_save = False


def search():
    global student_list, need_save, save_name

    if not student_list:
        print('No data to search')
        return
    
    while True:
        name = input('Enter the name to search for: ')

        if name.isalpha():
            break

        print('Please enter a valid name')
    
    found = False

    for student in student_list:
        print('Checked:', student.name)
        if name == student.name:
            found = True
            print(student.search())
            break
    
    if not found:
        print('Not Found')

def reset():
    global student_list, need_save, save_name

    save_first = 0
    if need_save:
        save_first = int(input('Do you want to save first? (0)no (1)yes: '))
    
    if save_first:
        save()

    clear_data()
    need_save = True
    print('Data cleared! Ready for new inputs.')

def clear_data():
    global student_list, need_save, save_name

    student_list.clear()
 
 
#main
quit = False
while not quit:
    print('1.Submit 2.Load 3.Summary 4.Display 5.Save 6.Search 7.Reset 8.Exit')
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
        save()
    elif choice == 6:
        search()
    elif choice == 7:
        reset()
    elif choice == 8:
        clear_data()
        save_name = None
        quit = True
    else:
        print('Invalid Choice!')