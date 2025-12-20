# Oop in Python       : Reusability and Modularity Real World projects 
# class -> Blueprint 
# Object -> Instance of a class
# Attributes -> Variables data 
# Methods -> Functions inside a class

class Vehicle:
    color="Red"  # Attribute
    petrol_type="Diesel"
    milage=15

# __init__ method -> Constructor
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model   


car1= Vehicle()
bike= Vehicle()
aeroplane= Vehicle()

print(car1.color)
print(bike.milage)
print(aeroplane.petrol_type)


class Student:
    #  whenever new obj of class is created __init__ method is called automatically

    def __init__(self, name, age, grade):
        self.name= name
        self.age= age
        self.grade= grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

std1= Student("Muhammad Khan", 20, "A+")
std1.display_info()

# pillors of OOP
# 1. Abstraction 
# essential things will be shared with user and hide the internal implemenation details
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number= account_number
        self.balance= balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")


#  2. Encapsulation
class Car:
    #   wrapping data and methods into single unit
    def __init__(self, brand, model, year):
        self.__brand= brand      # private attribute
        self.__model= model      # private attribute
        self.__year= year        # private attribute


# 3. Inheritance
# child class can inherit properties and methods from parent class
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
# 4. Polymorphism  ability to take many forms

class Cat(Animal):
    def speak(self):
        return "Meow!"






