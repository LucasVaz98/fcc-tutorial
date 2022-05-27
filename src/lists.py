# Using python to manipulate lists

'''
Python knows a number of compound data types, 
used to group together other values. The most
versatile of which is a list.
Others include:
    tuple
    dictionary
    set

Lists are written as a list of comma-separated values (items) between square brackets 
[1, 2, 3, 4]
['a', 'b', 'c']

Lists are mutable - this means that items can be changed
List have a bunch of methods available.
    append()->  Adds an element at the end of the list
    clear()-> 	Removes all the elements from the list
    copy()->  Returns a copy of the list
    count()-> 	Returns the number of elements with the specified value
    extend()->  Add the elements of a list (or any iterable), to the end of the current list
    index()->  Returns the index of the first element with the specified value
    insert()->  Adds an element at the specified position
    pop()->  Removes the element at the specified position
    remove()->  Removes the first item with the specified value
    reverse()->  Reverses the order of the list
    sort()->  Sorts the list

    LISTS ARE MUTABLE
'''


# The basics
squares = [1, 4, 9, 16, 25]
print(squares)

# The indexing in list is the same in strings, including with negative number to indicate a pos from the end to the start

print(squares[0]) #-> 1
print(squares[-1]) #-> 25
print(squares[-3:]) # [9, 16, 25]


# Create a list copy 
squares[:]

# Concatenation
squares_2 = squares + [36, 49]
print(squares_2) #-> [1, 4, 9, 16, 25, 36, 49]

# Alter items
cubes = [1, ,8, 27, 65, 125] # 65 is wrong here, so we wil change it!
cubes[3] = 64 # replace the wrong value YOU CAN'T DO IT WITH STRINGS, WHY?
print(cubes)


# Lists methods
cubes.append(216)
cubes.append(7 ** 6)
print(cubes)

# lenght
letters = ['a', 'b', 'c']
print(len(letters)) #-> Prints the number of characters, this case is 4

# Nesting
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x) #-> this will be a matrix! [['a', 'b', 'c'], [1, 2, 3]]
print(x[0]) #-> this wil print a, the first array in matrix
print(x[0][1]) #-> this will print 'b'


# List comprehension
y = []
for x in range(10):
    y.append(x ** 2)

print(y) #-> imprime todos os quadradados do números de 0  a 10 em uma lista


y = [x ** 2 for x in range(10)]
print(y) #-> Faz a mesma coisa, porém de uma maneira mais coesa de se ler


# Built-in functino list()
x = list(('bobby', 'at', 'didcoding', 'dot', 'com')) # create a list object


