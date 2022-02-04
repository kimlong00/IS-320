#3

#inputs
name = input('Enter your name: ')
num_books = int(input('Enter the number of books read: '))

#initializations
first_tier_points = 10
second_tier_points = 15
top_tier_points = 20

#computations
if num_books > 3:
    total_points = 3 * first_tier_points
    num_books = num_books - 3
else:
    total_points = num_books * first_tier_points
    num_books = 0

if num_books > 3:
    total_points = total_points + 3 * second_tier_points
    num_books = num_books - 3
else:
    total_points = total_points + num_books * second_tier_points
    num_books = 0

if num_books > 0:
    total_points = total_points + num_books * top_tier_points

#outputs
print(f'Member Name: {name:s}')
print(f'Total_points: {total_points:d}')