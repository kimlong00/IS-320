def is_even(number):
    #return true when number is even, False otherwise

    return number % 2 == 0

def is_commision_eligible(sales):
    return sales >= 1000.0



number = int(input('Enter an int '))
if is_even(number):
    print('Even!')
else:
    print('Odd!')