# Class definition for Car
class Car:
    # Method to simulate acceleration
    def accelerate(self):
        print("Car is speeding")  # Prints a message when the car accelerates

    # Method to simulate braking (note: corrected spelling from "brak" to "brake")
    def brake(self):
        print("Car is stopped")  # Prints a message when the car stops

# Creating an object (instance) of the Car class
c1 = Car()
c1.accelerate()  # Calls the accelerate method for c1

# Creating another instance of the Car class
c2 = Car()
c2.accelerate()  # Calls the accelerate method for c2

# Creating a third instance of the Car class
c3 = Car()
c3.accelerate()  # Calls the accelerate method for c3
c3.brake()  # Calls the brake method for c3
