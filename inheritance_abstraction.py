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


# Method Overriding Example in Python

# Parent class
class Fruit:
    # Method in parent class
    def fruit_info(self):
        print("Inside Parent Class")

# Child class inheriting from Fruit
class Apple(Fruit):
    # Overriding the fruit_info method from the parent class
    def fruit_info(self):
        # Calling the parent class method using super()
        super().fruit_info()
        print("Inside Child Class of Fruit Info")
    
    # Additional method specific to Apple class
    def apple_info(self):
        print("Inside Child Class - Apple Specific Info")

# Creating an object of Apple class
objs = Apple()
objs.fruit_info()  # Calls overridden method

# Example 2: Another subclass demonstrating method overriding
class Mango(Fruit):
    def fruit_info(self):
        super().fruit_info()
        print("Inside Mango Class - Fruit Info")

    def mango_info(self):
        print("Mango is known as the king of fruits.")

# Creating an object of Mango class
mango_obj = Mango()
mango_obj.fruit_info()  # Calls overridden method
mango_obj.mango_info()  # Calls class-specific method


# Multilevel Inheritance Example

# Base class (GrandFather)
class GrandFather:
    """
    This class represents the GrandFather level in the inheritance hierarchy.
    It has a method to display GrandFather's property.
    """
    def prop_grandfather(self):
        print("This is Grandfather's property")

# Intermediate class (Father) inheriting from GrandFather
class Father(GrandFather):
    """
    This class represents the Father level in the inheritance hierarchy.
    It inherits from GrandFather and adds its own property method.
    """
    def prop_father(self):
        print("This is Father's property. It includes both Father and Grandfather's property")

# Derived class (Son) inheriting from Father
class Son(Father):
    """
    This class represents the Son level in the inheritance hierarchy.
    It inherits from Father (which already inherits from GrandFather),
    thus gaining access to all ancestor properties.
    """
    def prop_son(self):
        print("This is Son's property. It includes Son, Father, and Grandfather's property")

# Creating an instance of Son and accessing properties
son = Son()
son.prop_father()      # Accessing Father's property
son.prop_grandfather() # Accessing GrandFather's property
son.prop_son()         # Accessing Son's property

print("\n--- Father Instance ---")
# Creating an instance of Father and accessing properties
fath = Father()
fath.prop_father()      # Accessing Father's property
fath.prop_grandfather() # Accessing GrandFather's property

print("\n--- GrandFather Instance ---")
# Creating an instance of GrandFather and accessing properties
graf = GrandFather()
graf.prop_grandfather() # Accessing GrandFather's property

# Another Example: Multilevel Inheritance in Vehicles

# Base class (Vehicle)
class Vehicle:
    """
    This class represents a general vehicle.
    """
    def vehicle_info(self):
        print("Inside Vehicle class")

# Intermediate class (Car) inheriting from Vehicle
class Car(Vehicle):
    """
    This class represents a Car, which is a type of Vehicle.
    It inherits from Vehicle and adds its own method.
    """
    def car_info(self):
        print("Inside Car class")

# Derived class (SportsCar) inheriting from Car
class SportsCar(Car):
    """
    This class represents a SportsCar, which is a specific type of Car.
    It inherits from Car (which inherits from Vehicle),
    thus gaining access to all ancestor methods.
    """
    def sports_car_info(self):
        print("Inside SportsCar class")

# Creating an instance of SportsCar and accessing methods
print("\n--- SportsCar Instance ---")
s1 = SportsCar()
s1.car_info()        # Accessing Car class method
s1.sports_car_info() # Accessing SportsCar class method
s1.vehicle_info()    # Accessing Vehicle class method
