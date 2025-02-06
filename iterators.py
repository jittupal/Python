# Iterators are used to get the values of an iterable one by one.
# They allow traversing through the elements without using indexing.
# An iterable is any object that can return its elements one at a time.
# Examples of iterables: strings, lists, tuples, sets, dictionaries.

# Example 1: Using a for loop to iterate over a string (iterable)
s = "jittupal"
for i in s:  
    print(i)  # Prints each character of the string one by one

print("\nUsing iter() and next() function:")

# Example 2: Using iter() and next() function on a string
a = iter(s)  # Creating an iterator from the string
print(next(a))  # Prints 'j'
print(next(a))  # Prints 'i'
print(next(a))  # Prints 't'
print(next(a))  # Prints 't'

# Example 3: Using iter() on a tuple
t = iter((1, 2, 3, 4, 5))  # Creating an iterator from a tuple
print(next(t))  # Prints 1
print(next(t))  # Prints 2
print(next(t))  # Prints 3

# Example 4: Using iter() on a set
# Note: Sets are unordered, so the output order may vary.
ss = iter({1, 4, 6, 8, 9, 0})  
print(next(ss))  # Prints a random value from the set
print(next(ss))  # Prints another random value
print(next(ss))  # Prints another random value

# Example 5: Using iter() on a dictionary
# Iterating over a dictionary returns keys by default.
d = iter({"jittu": "pal", "kittu": "pal"})  
print(next(d))  # Prints the first key (e.g., "jittu")
print(next(d))  # Prints the second key (e.g., "kittu")
