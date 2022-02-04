#2

#inputs
num_a = int(input("Enter an integer:  "))
num_b = int(input('Enter another integer:  '))

#outputs
if num_a == 0 or num_b == 0:
    print('Invalid input')
elif num_a == num_b:
    print('each is a factor of the other')
elif num_a % num_b == 0:
    print(f'{num_b:d} is a factor of {num_a:d}')
elif num_b % num_a == 0:
    print(f'{num_a:d} is a factor of {num_b:d}')
else:
    print('Neither is a factor of the other.')