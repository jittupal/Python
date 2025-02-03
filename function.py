import math as m  # Importing the math module and giving it an alias 'm'

# Using the ceil function to get the nearest highest integer value
print(m.ceil(7.6))  # Output: 8
print(m.ceil(9.1))  # Output: 10

# Using the floor function to get the nearest lowest integer value
print(m.floor(8.9))  # Output: 8
print(m.floor(2.1))  # Output: 2

# Defining a simple function that prints a greeting message
def greeting():
    print("welcome to the office")

greeting()  # Function call

greeting()  # Calling the function again

# Defining a function with a parameter 'name'
def greeting(name):
    print("welcome to the office", name)

greeting("ajay")   # Passing "ajay" as an argument

greeting("jittu")  # Passing "jittu" as an argument

# Defining a function that returns a string
def func():
    return "this is my first function"

print(func())  # Printing the returned value from func
print(func() + " in python")  # Concatenating and printing two strings

# Storing the return value of func in a variable
a = func()
print(a)  # Printing the stored value
print(type(a))  # Checking the data type of the return value (string)

# Defining a function that returns multiple values
def new_func():
    return "this is second", 1, 2.3, 3+4j  # Returning multiple values

# Unpacking the returned values into different variables
a, b, c, d = new_func()

print(a)  # Printing the first returned value (string)
print(b)  # Printing the second returned value (integer)
print(c)  # Printing the third returned value (float)
print(d)  # Printing the fourth returned value (complex number)
