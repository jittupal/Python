#string is a sequential representation of character
#each character is mapped with unique ASCII number
#strings are immutable

char = "a"
print(ord(char))  #it will print numberical value of character a

print(ord("A"))  #it will print 65

string1 = "jittu"
print(type(string1))

string2 = 'kittu'
print(type(string2))

#both of the above are way of initializing string

#concenate two strings

print(string1 + string2)

print("hello " + "world")

a = "jittu"

#accessing of character in string
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

#space is also counted as index
b = "i am jittu"

print(b[0]) 
print(b[1]) # it will print blank 

# slicing string in parts
print(b[0:4])  # it will only print the character from 0th index to 3 index (excluding 4)
print(b[5:9]) #it will only print the character from 5th index to 8th index (excluding 9)

print(a[3:]) #it will print the whole string from 3 index to last index
print(b[4:]) #it will print the whole string from index 4 to last index

print(b[-3:]) #it will print the last 3 character of string
print(b[-2:])  #it will only print the last 2 character of string

print(b[0:10:2]) #it will print the string in step of 2 distance

print(a[::-1])  #it will print the string in reverse character

print(len(b))  #it will include spaces as character in length
print(len(a))

#replacing word in string
a = a.replace("jittu", "mittu")
print(a)

b = b.replace("jittu", "student")
print(b)

#printing in lower case
c = "I AM JITTU"
print(c.lower())
c = c.lower()
print(c.upper()) #it will make every character of string in upper

#making first letter of every string should be in uppercase
print(c.title())

#make the first character in uppercase and rest in lower case
print(c.capitalize())

#searching in string
bio = "i am jittu and studying in pdsct college"
search = "littu"
if search in bio:
    print("word is present ")
else:
    print("word is not present")


email = "jittupal@gmail.com"
check_valid = "@"
if check_valid in email:
    print("email is valied")
else:
    print("email is invalid")

password = "jittupal"
length = len(password)
if length > 8:
    print("password accepted")
else:
    print("not accepted")

#check if each two string is equal or not

a = "jittu"
b = "jittu"

print(a == b) #true, because each character is same and in same case

a = "Jittu"
b = "jittu"

print(a == b) #false, because first character case is changed

#checking if the product code is matched with scanned code or not
product_code = "PV302"
scanned_code = input("Enter the scanned code:  ")
if product_code == scanned_code:
    print("You can go")
else:
    print("Talk to manager")