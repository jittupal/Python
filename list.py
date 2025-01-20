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