#tuples are immutable, it can not be change or modified after creation
#tuple is used to protect the data which we not want to change later
#tuple can also store multiple data types in it
#accessing of elements works same like list

new = (2, 3) 
print(type(new)) #it will print tuple

new_list = (2, 3.3, "jittu", (3+4j), False)
print(type(new_list)) #the type is list

print(new_list[3]) #it will print 3+4j
print(new_list[-3]) #it will print jittu

# new_list[4] = True #it will give error because we can't change tuples values

#mutiple tuples can be stored in a single tuple
box1 = ("a", "b")
box2 = ("c", "d")
cho_bag = (box1, box2)

print(cho_bag)

#accessing a item of tuple in a tuple
print(cho_bag[1][1]) #it will print d
print(cho_bag[0][0]) #it will print a

for box in cho_bag:    #it will access the box one by one
    for choc in box:    #it will access the element of box one by one
        print(choc)      

# Creating a tuple named tuple1 with repeated elements
tuple1 = ("jittu", "jittu", 1, 2, 3, 3, 3, 4, "jittu")

# Counting occurrences of the number 3 in the tuple
print(tuple1.count(3))  # Output: 3 (since 3 appears three times)

# Counting occurrences of the string "jittu" in the tuple
print(tuple1.count("jittu"))  # Output: 3 (since "jittu" appears three times)

# Finding the index of the first occurrence of the number 3
print(tuple1.index(3))  # Output: 4 (zero-based index, so the first 3 appears at position 4)

# Finding the index of the first occurrence of the string "jittu"
print(tuple1.index("jittu"))  # Output: 0 (the first occurrence is at index 0)

# Slicing the tuple from index 3 to 6 (excluding 6)
print(tuple1[3:6])  # Output: (2, 3, 3) (extracts elements at indices 3, 4, and 5)

# Reversing the tuple using slicing
print(tuple1[::-1])  # Output: ('jittu', 4, 3, 3, 3, 2, 1, 'jittu', 'jittu') (full tuple reversed)
