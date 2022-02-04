"""Lists"""
#Data structures
#Lists,  Dictionaries, Tuples , Sets
#lists []  dict  {}

#functions
#lists can be inputs to functions

#sum elements of a list   in: list  out: sum

#product of elements in a list



#find highest element in a list


#algorithms + data structures

def print_list(my_list, sep = '\n'): #optional paramter
    for x in my_list:
        print(x, end = sep)
    if sep != '\n':
        print()

def print_squares(list):
    for element in list:
        print(element * element)

def make_squares(list):
    squares = []
    for item in list:
        squares.append(item * item)

    return squares

def find_max(list):
    max = list[0]
    for x in list:
        if x > max:
            max = x

    return max

def find_min(list):
    min = list[0]
    for x in list:
        if x < min:
            min = x

    return min

def search(key, list):
    if key in list:
        print('Found', list.index(key))
    else:
        print('Not Found')


#main
#make a list
numbers = [4,5,6,10,3]
# print(numbers)
# for num in numbers:
#     print(num)

print_list(numbers, ' ')
# print_list(numbers)
#print the list 
# print_squares(numbers)

# print_list(make_squares(numbers))

print(numbers[0], numbers[1], numbers[4], numbers[-1])
numbers.append(100)
print(numbers[0], numbers[1], numbers[4], numbers[-1])

colors = ['Red', 'Green', 'Blue']
print_list(colors)

some_list = [10, 'Red', True, 1.5]
print_list(some_list)

print(find_max(numbers))
print(find_min(numbers))

#search

# key = int(input('Enter an integer: '))

# if key in numbers:
#     print('Found', numbers.index(key))
# else:
#     print('Not Found')

# #iterate (loop) through the list, and print each 'element'
# 

# #for <element> in <list>  loop
# 
# 

# #loop through the list and do computations with each element

# #print square of each number
# 

# #add more elements
# 

# 

# #index and value    access individual elements in a list
# #index start at 0
# 



# #emptying a list
# 

# 
#lists and functions
#


#function returning list


#count elements in a list

#DIY make a function  input: list  output: count   

#sum elements in a list
#product of elements in a list





#find highest element in a list

#find lowest element in a list  


#NOTES
#Making a list 
#1.  initialize an empty list, and append each value as we receive, or compute the value.
# we use this when we don't know all the values beforehand, and we don't know how many values there will be.

#2. create and store all values at once.   numbers = [10,100, 50]
#3. call a function that brings back a list.  mylist = make_squares(numbers)
#4. say you have name, age, income as three variables (with values in them)
#  input_list = [name,age,income]

#list can be sent in as input to a function
#a function can return a list as output

# numbers.clear()  #the right way to empty out, or reset a list.


# numbers = [] #this is good for initializing numbers as an empty list.
# #this is not good for: resetting a list

#for reference only:
# for index,value in enumerate(numbers):
#     print(index,value)