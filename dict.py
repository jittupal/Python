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