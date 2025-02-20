# Inheritance in Python

## Definition
#Inheritance is an object-oriented programming (OOP) concept where a class (child class) derives properties and behaviors from another class (parent class). It helps in code reusability and establishing a relationship between different classes.

# Single Inheritance Example 1
## Definition
#Single inheritance is a type of inheritance where a child class inherits from only one parent class. This allows the child class to reuse the properties and methods of the parent class.

### Example 1: Parent and Child Relationship
# Parent class
class Father:
    def father_property(self):
        print("This is father's property")

# Child class inheriting from Father
class Son(Father):
    def job(self):
        print("Son has property from job")

# Creating an instance of the Son class
child_obj = Son()

# Calling methods from both child and parent classes
child_obj.job()  # Calls the method defined in Son class
child_obj.father_property()  # Calls the inherited method from Father class

# Creating an instance of the Father class
father_obj = Father()
father_obj.father_property()  # Father can only access its own methods

print("\n")  # Just for separating outputs

# Single Inheritance Example 2
## Definition
#This example demonstrates single inheritance where a child class inherits properties from a parent class representing fruits.

### Example 2: Fruit and Apple Relationship
# Parent class
class Fruit:
    def fruit_info(self):
        print("It is a parent class representing general fruits")

# Child class inheriting from Fruit
class Apple(Fruit):
    def apple_info(self):
        print("It is a child class representing a specific type of fruit: Apple")

# Creating an instance of Apple class
obj = Apple()

# Calling methods from both child and parent classes
obj.apple_info()  # Calls the method from Apple class
obj.fruit_info()  # Calls the inherited method from Fruit class
