#Using python as a calculator

'''
We can use the interpreter to take an input and return an output

Aritmetic Operators:
    We have a whle bunch of operators at our disposal
    + Addition
    - Subtraction
    * Multiplication (always return a float) 
    / Division
    // Floor Division
    % Modulus (remainder of x/y) | use divmod(a, b)
    ** Exponentiation (power of) | can also use pow(x, y) instead of x**y

    Assignment Opperators:
        = Equals

    Numbers Types: 
        int(2, 3, 4123, 4567345)
        float(1.2, 3.5344, 5.63445234)

    Build in Functions:
        round() Rounds a number with the specified number of
        decimals, i.e round(number, decimals)

        lastly, Python has a handy way of making big int's easier to read 
        4000000000 can be writen as 4_000_000_000
'''

print(10 / 4) #Classic division returns a float
print(10 // 4) #Floor division discards the fractional part 
print(10 % 4) # the % operator returns the ramainder of the division
print(divmod(10, 4)) # Same thing here, but divmod returns a tuple of the result of the floor division

# Fancy sums
print(50 - 5*6)
print((50 - 5*6)/4)
print(5 * 3 + 2) # Floored quotient * divisor + remainder

# Exponentiation (power of)
print(5 ** 2) # 5 squared
print(2 ** 7) # 2 to the power of 7
print(pow(2,7)) # same thing here

# Using varibles
width = 60
height = 3 * 7
print(width)
print(height)
print(width * height)

# In interactive mode, the last printed expression is assigned to the variable _.

tax = 12.5 / 100
price = 100.50

print(price * tax)# this is assigned to '_' and we use it in the next expression
print(price + _) # We referece '_' but this expression is now assignd to '_'
print(_, 2)
