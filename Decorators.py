# Definition: A decorator is a function that takes another function as an argument
# and extends its behavior without modifying the original function's structure.

# Example 1: A basic decorator that prints messages before and after the function execution.
def my_decorator(func):
    def wrapper():
        print("Before Computation:")  # This runs before the function execution
        func()  # Calling the original function
        print("After Computation:")  # This runs after the function execution
    return wrapper  # Returning the inner function

# Using the decorator with a simple function
@my_decorator
def say_hello():
    print("Hello World")

say_hello()

# Another example using the same decorator
@my_decorator
def sum_numbers():
    print("3 + 4:", 3 + 4)  # Simple arithmetic operation

sum_numbers()

# Example 2: A decorator to measure execution time of functions
import time  # Importing time module for performance measurement

def time_decorator(func):
    def timer():
        start = time.time()  # Start time before function execution
        func()  # Execute the function
        end = time.time()  # End time after function execution
        print("The time for executing the code:", end - start)  # Calculate elapsed time
    return timer

# Using the execution time decorator
@time_decorator    
def func_test():
    print("11 * 1000:", 11 * 1000)  # Multiplication operation

func_test()

# Another function using the time decorator
@time_decorator
def print_name():
    print("My name is Jittu")

print_name()

# Additional Example: Decorator to convert output to uppercase

def uppercase_decorator(func):
    def wrapper():
        result = func()  # Call the function
        return result.upper()  # Convert result to uppercase
    return wrapper

@uppercase_decorator
def greet():
    return "Hello, welcome to decorators!"

print(greet())  # Output will be in uppercase
