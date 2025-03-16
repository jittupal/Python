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

