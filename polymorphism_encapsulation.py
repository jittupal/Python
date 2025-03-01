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
