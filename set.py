#sets are unordered collection of unique elements
#we can also add different types of data
#it is mutable


s = {"jittu", "kittu"}  #declaration of sets
print(type(s)) #it will print set

a = {"orange", "apple", "apple", "orange", "mango"}
print(a) #it will only print one item only one time

#adding an element to set
s.add("mittu") 
print(s)

s.remove("jittu") #this will remove the element from the set
print(s)

#accessing the elements of set
for item in a:
    print(item)