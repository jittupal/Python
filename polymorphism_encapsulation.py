# Polymorphism in Python
# Polymorphism allows us to define a single interface and have multiple implementations.
# It helps in writing more generic and reusable code.

# Example 1: Function Polymorphism

def func(a, b):
    """
    This function demonstrates polymorphism by adding different types of objects.
    It works for integers, strings, and lists.
    """
    print(a + b)

# Calling function with different data types
func(4, 6)  # Adding integers
func("Jittu ", "Pal")  # Concatenating strings
func([1, 2, 3], [4, 5, 6])  # Merging lists

# Example 2: Class Polymorphism

class Teacher:
    """Class representing a Teacher."""
    def name_of(self):
        print("This is the class of Teacher")

class Student:
    """Class representing a Student."""
    def name_of(self):
        print("This is the class of Student")

# Creating objects of Teacher and Student
obj1 = Teacher()
obj2 = Student()

# Storing objects in a list
class_obj = [obj1, obj2]

# Function demonstrating polymorphism with classes
def parcer(class_obj):
    """
    This function takes a list of objects and calls their 'name_of' method.
    It works because both classes have the same method name, demonstrating polymorphism.
    """
    for i in class_obj:
        i.name_of()

# Calling the function
parcer(class_obj)

# Example 3: Polymorphism with Built-in Methods

print(len("Hello"))  # len() works on strings
print(len([1, 2, 3, 4]))  # len() works on lists
print(len({1: "one", 2: "two"}))  # len() works on dictionaries

# Example 4: Polymorphism with Inheritance

class Animal:
    """Base class representing an Animal."""
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    """Derived class representing a Dog."""
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    """Derived class representing a Cat."""
    def speak(self):
        return "Cat meows"

# Function demonstrating polymorphism
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.speak())


# Definition: 
# Method Overloading is a concept in object-oriented programming where multiple methods in the same class 
# have the same name but different parameters. However, Python does not support traditional method overloading.
# Instead, only the last defined method is used, as seen in the example below.

# Method Overloading Example (Python does not support traditional overloading)
class Student:
    def student(self):
        print("Welcome Student")

    def student(self, name=""):  # This method overrides the previous one
        print("Welcome in the class:", name)

    def student(self, course="", name=""):  # This method overrides the previous ones
        print("Welcome", name, "in the class of", course)

# Creating an object of the Student class
stu = Student()

# Calling the method with different arguments
stu.student()  # Calls the last defined method with default values
stu.student("Jittu")  # Calls with one argument
stu.student("Devops", "Jittu")  # Calls with two arguments

# Another class with the same method definition
class Student:
    def student(self, course="", name=""):
        print("Welcome in the class,", course, name)

# Creating an object of the second Student class
stu = Student()

# Calling the method with different arguments
stu.student()  # Calls the method with default values
stu.student("Jittu")  # Calls with one argument
stu.student("Devops", "Jittu")  # Calls with two arguments

# Additional Example: Using variable arguments (*args) to handle multiple cases
class Calculator:
    def add(self, *args):  # Accepts a variable number of arguments
        return sum(args)

# Creating an object of the Calculator class
calc = Calculator()

# Calling the method with different numbers of arguments
print(calc.add(5, 10))  # Calls with two arguments
print(calc.add(5, 10, 15))  # Calls with three arguments
print(calc.add(5, 10, 15, 20))  # Calls with four arguments


# Method Overriding in Python
# ----------------------------------
# Definition:
# Method Overriding is a feature in object-oriented programming where a child class 
# provides a specific implementation of a method that is already defined in its parent class. 
# The method in the child class must have the same name as in the parent class.

# Example 1: Basic Method Overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")  # Parent class method

class Cat(Animal):
    def sound(self):
        print("Cat meows")  # Overriding the parent class method

# Creating instances and calling methods
anm = Animal()
anm.sound()  # Calls the parent class method

cat = Cat()
cat.sound()  # Calls the overridden method in the child class


# Example 2: Another Method Overriding Example
class Vehicle:
    def speed(self):
        print("Vehicles have different speeds")

class Car(Vehicle):
    def speed(self):
        print("A car runs at an average speed of 100 km/h")

# Creating instances
veh = Vehicle()
veh.speed()  # Calls the parent class method

car = Car()
car.speed()  # Calls the overridden method in the child class


# Example 3: Using Method Overriding with Multiple Levels of Inheritance
class Bird:
    def fly(self):
        print("Birds can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrows fly at a moderate height")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

# Creating instances
bird = Bird()
bird.fly()  # Calls the parent class method

sparrow = Sparrow()
sparrow.fly()  # Calls the overridden method in Sparrow class

penguin = Penguin()
penguin.fly()  # Calls the overridden method in Penguin class


# Encapsulation in Python

# Definition:
# Encapsulation is one of the core principles of Object-Oriented Programming (OOP).
# It is used to restrict direct access to variables and methods to prevent unintended modifications.
# Encapsulation is implemented using access modifiers like public and private.

# ---------------- PUBLIC ACCESS ----------------
# Public attributes can be accessed directly outside the class.

class Student:
    # Constructor to initialize student name and degree
    def __init__(self, name, degree):
        self.name = name  # Public attribute
        self.degree = degree  # Public attribute

# Creating student objects
stud1 = Student("Jittu", "CS")
stud2 = Student("Kittu", "EE")

# Accessing public attributes
print(stud1.name)  # Output: Jittu
print(stud1.degree)  # Output: CS

print(stud2.name)  # Output: Kittu
print(stud2.degree)  # Output: EE

# Public attributes can be modified outside the class
stud2.degree = "IT"  # Changing the degree of stud2
print(stud2.degree)  # Output: IT

# Example with a method inside the class
class Student:
    def __init__(self, name, degree):
        self.name = name  # Public attribute
        self.degree = degree  # Public attribute

    # Public method to display student details
    def show(self):
        print("Name:", self.name, "Degree:", self.degree)

# Creating an object
aj = Student("Ajay", "CS")
aj.show()  # Output: Name: Ajay Degree: CS

# Accessing public attributes
print(aj.name)   # Output: Ajay
print(aj.degree) # Output: CS


# ---------------- PRIVATE ACCESS ----------------
# Private attributes are indicated by a double underscore ( __ )
# They cannot be accessed directly outside the class.

class Student:
    def __init__(self, name, degree):
        self.name = name  # Public attribute
        self.__degree = degree  # Private attribute

    # Public method to display student details
    def show(self):
        print("Name:", self.name, "Degree:", self.__degree)

# Creating an object
aj = Student("Ajay", "CS")
aj.show()  # Output: Name: Ajay Degree: CS

# Accessing public attribute
print(aj.name)  # Output: Ajay

# Trying to access private attribute directly (will cause an error)
# print(aj.__degree)  # This will raise an AttributeError

# Accessing private attribute using name mangling
print(aj._Student__degree)  # Output: CS

class User:
    def __init__(self, username, password):
        self.username = username  # Public Attribute
        self.__password = password  # Private Attribute

    # Method to check password (simulating login)
    def check_password(self, input_password):
        if self.__password == input_password:
            print("Login successful!")
        else:
            print("Invalid password!")

# Creating user object
user1 = User("john_doe", "secure123")

# Accessing public attribute
print(user1.username)  # Output: john_doe

# Trying to access private attribute (will cause an error)
# print(user1.__password)  # This will cause an AttributeError

# Checking password using method
user1.check_password("secure123")  # Output: Login successful!
user1.check_password("wrongpass")  # Output: Invalid password!

# Accessing private attribute using name mangling (not recommended)
print(user1._User__password)  # Output: secure123
