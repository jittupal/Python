# Lambda Function: A short, anonymous function that can have multiple arguments but only one expression.

# Lambda function to calculate the square of a number
square_lambda = lambda x: x**2  # Takes 'x' as input and returns x squared

# Calling the square_lambda function with different values
ans = square_lambda(5)  
print(ans)  # Output: 25

ans = square_lambda(6)  
print(ans)  # Output: 36

ans = square_lambda(9)  
print(ans)  # Output: 81

# Lambda function to add two numbers
add = lambda a, b: a + b  # Takes 'a' and 'b' as inputs and returns their sum

# Calling the add function with different values
ans = add(3, 5)  
print(ans)  # Output: 8

ans = add(8, 5)  
print(ans)  # Output: 13

ans = add(8, 8)  
print(ans)  # Output: 16

# Lambda function to check if a number is even
even = lambda x: x % 2 == 0  # Returns True if 'x' is even, otherwise False

# Checking if the given numbers are even
ans = even(7)  
print(ans)  # Output: False (7 is odd)

ans = even(4)  
print(ans)  # Output: True (4 is even)

ans = even(9)  
print(ans)  # Output: False (9 is odd)

# A list of strings
lists = ["jittu", "pal", "cs", "final-year"]

# Sorting the list alphabetically
x = sorted(lists)
print(x)  # Output: ['cs', 'final-year', 'jittu', 'pal']

# Sorting the list based on the length of each element
sorted_by_length = sorted(x, key=lambda x: len(x))
print(sorted_by_length)  # Output: ['cs', 'pal', 'jittu', 'final-year']

# Another example: sorting names based on length
names = ['a', 'bc', 'b', 'der', 'ki', 'kamo', 'kii']

# Sorting the list of names based on their length
y = sorted(names, key=lambda name: len(name))
print(y)  # Output: ['a', 'b', 'bc', 'ki', 'der', 'kii', 'kamo']

# Lambda function to calculate Fibonacci series
fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)

# Generating the first 10 Fibonacci numbers using list comprehension
ans = [fib(i) for i in range(10)]
print(ans)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Function to calculate factorial using recursion
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))  # Output: 120 (5! = 5*4*3*2*1)

# Lambda function to calculate factorial
fact_num = lambda x: 1 if x == 0 else x * fact_num(x-1)
print(fact_num(7))  # Output: 5040 (7! = 7*6*5*4*3*2*1)

# Using map function to apply a function to each element of a list

# Function to calculate square
def sq(x):
    return x ** 2

l = [1, 2, 3, 4, 5, 6]

# Applying square function to each element in the list
square_list = list(map(sq, l))
print(square_list)  # Output: [1, 4, 9, 16, 25, 36]

# Function to add 10 to each element
def add(x):
    return x + 10

add_list = list(map(add, l))
print(add_list)  # Output: [11, 12, 13, 14, 15, 16]

# Function to multiply each element by 2
def mul(x):
    return x * 2

mul_list = list(map(mul, l))
print(mul_list)  # Output: [2, 4, 6, 8, 10, 12]
