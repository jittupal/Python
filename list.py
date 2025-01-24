#list can store anything or it can store all the data types in it. 
#list is mutable, it can be updated or changed anytime
#list start with 0 and end with n-1
#from reverse item can be accessed with negative values start from -1 to number to elements

num = [1 ,2 , 3, 4, 5]
print("type: ", type(num))  #type == list

print(num)  #it will print all the data stored in num list

print(num[2])  #it will print 3
print(num[-1]) #it will print 5
print(num[-5])  #it will print 1

all_list = [2, 3.3, "jittu", False, (3+2j)] #it has all the data types in the list

print(type(all_list[-1]))  #it will print complex

#adding element to list
all_list.append("kittu") #it will add element kittu in the end of the list
print(all_list)

all_list.append("kittu")
print(all_list)
print(all_list[6]) #it has value = kittu

#index 5 and 6 has value = kittu

all_list.remove("kittu")  #it will remove first occurence of element , it will remove kittu of 5th index
print(all_list)


#storing list in list
new_list = [2, 3, "jittu", [3, 5, 7]]
print(new_list[3][1]) #it will print 5 from second list in it

a_list = [[2, 3, 4], [1 , 2, 3], [7, 8, 9]]
print(a_list[2]) #it will print all 3 list

all_list[3] = True #it will change the value of 3 index in all_list from false to true
print(all_list)

all_list[4] = 5+6j #it will change the value of inndex 4 from 3+2j to 5+6j
print(all_list)

for item in all_list:
    print(item, end=" ")

print()
lis = ["apple", "mango", "orange", "banana"]
lis.insert(1, "pineapple") #this will add pineapple before 1st index
print(lis)

lis1 = ["apple", "banana", "orange"]
lis2 = ["pineapple", "watermelon", "kivi"]
lis1.extend(lis2)  #this will add elements of lis2 in the lis1
print(lis1)

#repeatation
lis3 = ["jittu"]
lis3 = lis3 * 3 #it will add jittu 3 times in lis3
print(lis3)

lis4 = [12]
lis4 = lis4 * 5
print(lis4)

lis5 = list(range(10)) #it will make a list of containing element from 0 to 9
print(lis5)

lis6 = list(range(0, 11, 2)) #it will make a list of even numbers
print(lis6)

#checking if the element is present or not in the list
ans = "potato" in lis1  #it will check if the potato is in the lis1
print(ans)

ans = "orange" in lis1
print(ans)  #true

ans = "mango" not in lis1  #it will check if the element is not present in the list
print(ans)

ans = "banana" not in lis1
print(ans)

#shallow copy
name = ["jittu", "kittu", "mittu"]
new_lis = name   #it will copy all the elements of name list into new_lis
print(new_lis)

name.insert(2, "chittu")  #if we change in name list then it will also affect new lis
print(name)
print(new_lis) #new lis also have the updated element at the same index

new_lis.insert(2, "littu") #new lis changes will also shown in name list
print(new_lis)
print(name)

#deep copy

b = name.copy()  #it will copy the element of name into b
print(b)

name.remove("littu")  #it will not affect the other list
print(name)   #it one value is deleted
print(b)  #it will remain same

#sorting of list
print(sorted(name))  #it will short the element by alphabetic
print(sorted(lis1))

#index function
value = name.index("chittu")  #it will store the first index of element
print(value)

value = lis1.index(lis1[3])
print(value)

#lenght of list
print(len(lis1)) #it will print total number of element present in lis1
print(len(name))