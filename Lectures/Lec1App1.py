"""Lec1App1.py Developed by Kimklong 09.30.21.

This app computes and displays order price for
books, given the price per book.
Inputs (from user):  number of books (int)
Outputs: order price. (float). """

#Initialization
price_per_book = 1.5

#inputs
user_name = input('Enter your name?>> ')
num_books = int(input('And how many books are you ordering today?>> '))
#price_per_book = float(input("What is the unit price?>> "))

#computations
order_price = price_per_book * num_books

#outputs
#Hi, You ordered 10 books, and the order price is 15 Dollars.
print(f"Hi {user_name:s}, You ordered {num_books:d} books, and the order price is ${order_price:.2f} Dollars.")

#string formatting codes    int d   float f    str s
#all print should use f formatting f'....'
#all floats should be printed with .xf





# you have x and with to convert it to an int
#int(x)
#typename(x)


#num_books = int(input('And how many books are you ordering today?>> '))
#num_str = input("How many books?") # '100'
#num_books = int(num_str) * num_books