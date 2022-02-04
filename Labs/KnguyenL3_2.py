#2

#inputs
num_books = int(input('Enter the number of books ordered: '))
book_status = int(input('Is the the book online(1) or offline(0): '))

#initializations
book_price = 15.0
shipping_rate = 0.25
tax_rate = 0.08

#computations
if book_status:
    if num_books > 10:
        shipping_cost = 5.0
    else:
        shipping_cost = num_books * shipping_rate   
    total_cost = num_books * book_price + shipping_cost
else:
    tax = num_books * book_price * tax_rate
    total_cost = num_books * book_price + tax

#outputs
if book_status:
    print(f'Total cost is ${total_cost:.2f} including shipping of ${shipping_cost:.2f}')
else:
    print(f'Total cost is ${total_cost:.2f} including a tax of ${tax:.2f}')
