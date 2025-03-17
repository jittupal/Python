# use of predefined keywords in Python


num = 10

if num > 0:
    print("Positive number")  
elif num < 0:
    print("Negative number")  
else:
    print("Zero")  


for i in range(5):
    print(i)  

count = 0
while count < 3:
    print(count)  
    count += 1

for i in range(5):
    if i == 3:
        break  
    print(i)

for i in range(5):
    if i == 2:
        continue  
    print(i)

my_list = [1, 2, 3]
print("Before modification:", my_list)

my_list[0] = 10  # Modifies the first element
print("After modification:", my_list)

my_dict = {'name': 'Alice', 'age': 25}
print("Before modification:", my_dict)

my_dict['age'] = 26  # Changing value of an existing key
my_dict['city'] = 'New York'  # Adding a new key-value pair
print("After modification:", my_dict)

my_set = {1, 2, 3}
print("Before modification:", my_set)

my_set.add(4)  # Adding a new element
my_set.remove(2)  # Removing an element
print("After modification:", my_set)


my_string = "Hello"
print("Original string:", my_string)

# Trying to modify a string
# my_string[0] = 'h'  #This will cause an error

my_tuple = (1, 2, 3)
print("Original tuple:", my_tuple)

# my_tuple[0] = 10  # This will cause an error
