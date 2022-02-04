#function

def show_greeting(msg):
    print(msg)

def compute_price(wt):
    unit_price = 15.0
    price = wt * unit_price
    return price

order_price = compute_price(10.0)
print(order_price)

#call or invoke the function
show_greeting('Good Afternoon')
show_greeting('Hello there')
show_greeting('Bye!')
output = 'Farewell'
#msg = 'Bye!'
show_greeting(output)
#the value otput goes to the variable msg
#msg = ouput 

#pi * radius squared


def test(s, k):
    print(s * k)

test(9, 6)