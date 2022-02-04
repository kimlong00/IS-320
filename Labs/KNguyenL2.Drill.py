#1. User enters an integer. Your app displays ‘Positive’, ‘Negative’, or ‘Zero’ based on its value.
# number = int(input('Enter a number:  '))

# if number > 0:
#     print('Positive')
# elif number == 0:
#     print('Zero')
# else:
#     print('Negative')

#2
# grade = float(input('Enter a number grade:  '))

# if grade >= 90:
#     print('A')
# elif grade >= 80:
#     print("B")
# elif grade >= 70:
#     print('C')
# elif grade > 60:
#     print('D')
# elif grade == 60:
#     print('P')
# else:
#     print('F')

# #3
# a = 16
# b = 12
# c = 18

# if a > b:
#     if a > c:
#         print("a")
#         print(a)
#     else:
#         print('c')
#         print(c)
# elif b > c:
#     print('b')
#     print(b)
# else:
#     print('c')
#     print(c)

#4.1
# first_num = int(input("Enter the first number: "))
# second_num = int(input('Enter the second number: '))
# number_of_elements = int(input('Enter the number of elements: '))
# num_difference = second_num - first_num

#sum_series = (number_of_elements * (2 * first_num + (number_of_elements - 1) * num_difference))/2
#print(sum_series)

#4.2
# first_num = int(input("Enter the first number: "))
# second_num = int(input('Enter the second number: '))
# last_num = int(input('Enter the last number: '))

# num_difference = second_num - first_num
# number_of_elements2 = 1 + (last_num - first_num) / num_difference
# sum_series2 = (number_of_elements2 * (2 * first_num + (number_of_elements2 - 1) * num_difference))/2

# print(sum_series2)

#5. Not bug Free
# sample_char = input('Enter a character: ')

# if sample_char >= 'a':
#     print('Lower case')
# elif sample_char >= 'A':
#     print('Upper Case')
# elif sample_char >= '0':
#     print('digit')
# elif sample_char < '0':
#     print('digit')
# else:
#     print('Other')

#6.

# num1 = 10
# num2 = 3
# num3 = 6.5
# num4 = 1.5

# print(num1 // num2)
# print(num1 % num2)
# print()
# print(num3 // num4)
# print(num3 % num4)
