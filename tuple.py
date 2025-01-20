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