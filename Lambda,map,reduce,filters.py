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
