"""
the price of a book changes based on number of books ordered.
1-10 books  $15
>10-100     $12
>100    $10

read number of books ordered from user, and display order price.
"""

num_books = int(input('Number of books purchased:   '))

if num_books <= 10:
    book_price_unit = 15.0
elif num_books <= 100:
    book_price_unit = 12.0
else:
    book_price_unit = 10.0

total_cost = book_price_unit * num_books

print(f'You ordered {num_books:d} books')
print(f'Price per book: ${book_price_unit:.2f}')
print(f'Total cost: ${total_cost:.2f}')