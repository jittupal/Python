#dictionaries are un-ordered collections of key, value pairs
#each key must be unique
#dictionaries are mutable

#creation of dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"} 
print(my_dict)

print(type(my_dict))  #this will print dict

#accessing value in dictionary
name = my_dict["name"] 
print(name)  # Output: Alice

age = my_dict.get("age") 
print(age)   # Output: 30

#adding or modifing value in dictionary
my_dict["occupation"] = "Engineer"  # Add a new key-value pair
my_dict["age"] = 31                  # Modify an existing value
print(my_dict)

#removing value in dictionary
del my_dict["city"]  # Remove the "city" key-value pair
city = my_dict.pop("occupation")  # Remove and return the value of "occupation"
print(my_dict)
print(city)

#iterating through a dictionary
for key in my_dict:
    print(key, ":", my_dict[key]) 

for key, value in my_dict.items():
    print(key, ":", value)

print(my_dict.values())  #it will only print the value of dictionary 
print(my_dict.keys()) #it will only print the keys of dictionary

# Creating a dictionary named 'details' with some personal information
details = {"name": "jittu", "age": 21, "phone": 21212121, "email": "jittupal@yahho.com"}

# Printing the entire dictionary
print(details)

# Accessing and printing specific values using their keys
print(details["name"])   # Prints the value associated with the key "name"
print(details["email"])  # Prints the value associated with the key "email"

# Adding new key-value pairs to the dictionary
details["address"] = "mp"   # Adding an address field
details["student"] = "yes"  # Indicating if the person is a student

# Modifying an existing value in the dictionary
details["name"] = "kittu"   # Changing the name from "jittu" to "kittu"

# Printing the updated dictionary
print(details)

# Creating another dictionary with different key types (float, boolean, complex number, and string)
new_dict = {1.2: "jittu", True: "student", 2+3j: "complex", "elgible": "yes"}

# Accessing and printing values using their respective keys
print(new_dict[1.2])    # Prints the value for key 1.2 (float)
print(new_dict[True])   # Prints the value for key True (boolean)

# The below line is commented out because it would cause an error.
# Dictionary keys must be immutable (unchangeable types like strings, numbers, or tuples),
# but sets are mutable, so they cannot be used as dictionary keys.
# new_dict = {{1, 2, 3}: "ajay"}

# Printing the dictionary
print(new_dict)
