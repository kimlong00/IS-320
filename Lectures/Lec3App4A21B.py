"""
20 // 3 = 6
20 % 3 = 2

21 % 3 = 0

x % 2 = 0   => x is even
"""

# read an integer from the user, and check if it is even or odd.
#if it is an even number, else check if it is divisible by 3
#also include a print stating a number is not divisible by 6
number = int(input("Enter a whole number: >> "))

if number % 2 == 0:
    print('even')
    if number % 3 ==0:
        print('divisible by 6 as well')
    else:
        print('not dvisible by 6 as well')
else:
    print('odd')
    print('not divisible by 6')
