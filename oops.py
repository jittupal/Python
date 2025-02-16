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

# Define a class named 'Bank'
class Bank:
    # Class attribute 'amount' which represents the initial balance of the bank account
    amount = 10000  

    # Method to deposit money into the account
    def deposit(self, amount_dep):
        print(f"I am depositing {amount_dep} money")  # Print deposit message
        self.amount = self.amount + amount_dep  # Add the deposited amount to the total balance

    # Method to withdraw money from the account
    def withdraw(self, amount_withdraw):
        self.amount = self.amount - amount_withdraw  # Subtract the withdrawn amount from the total balance
        print(f"I am withdrawing {amount_withdraw} money")  # Print withdrawal message

    # Method to check the remaining balance
    def remain(self):
        print(f"Available balance is {self.amount} money")  # Print the available balance

# Create an object (instance) of the 'Bank' class
b = Bank()

# Deposit 2000 into the bank account
b.deposit(2000)  # New balance = 10000 + 2000 = 12000
b.remain()  # Prints: Available balance is 12000 money

# Withdraw 2000 from the bank account
b.withdraw(2000)  # New balance = 12000 - 2000 = 10000
b.remain()  # Prints: Available balance is 10000 money

# Deposit 5000 into the bank account
b.deposit(5000)  # New balance = 10000 + 5000 = 15000

# Withdraw 3000 from the bank account
b.withdraw(3000)  # New balance = 15000 - 3000 = 12000

# Check remaining balance
b.remain()  # Prints: Available balance is 12000 money
