# Classes and Obejects


# class Mayur:
#     name="Mayuresh"
#     address="Shrirampur"
#     grade="A"
#     def greet(self):  #this is method
#         print(f"Hello my name is {self.name} and my address is {self.address} and passed with {self.grade} grade !!")
#
# m= Mayur()
# print(m.name)
# print(m.address)
# print(m.grade)
#
# m.greet()  #calling method

#Output
# Mayuresh
# Shrirampur
# A
# Hello my name is Mayuresh and my address is Shrirampur and passed with A grade !!


# With __init__
# class Mayur:
#     def __init__(self, name, address, grade):  #__init__ used for more dynamic ,reusable and scalable for program
#         self.name = name
#         self.address = address
#         self.grade = grade
#
#     def greet(self):
#         print(f"Hello my name is {self.name}, my address is {self.address}, and I passed with {self.grade} grade!!")
#
# # Creating an object with dynamic values
# m = Mayur("Mayuresh", "Shrirampur", "A")

# Accessing attributes
# print(m.name)
# print(m.address)
# print(m.grade)

# Calling the greet method
# m.greet()





# class Person:
#     def __init__(self, name):
#         self.name = name
#
# # Create an object of the Person class
# p = Person("Mayuresh")
# print(f"Person's name is: {p.name}")

# Output:
# Person's name is: Mayuresh



# Creating a Car Class with Methods
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def display_car(self):
#         print(f"Car: {self.brand} {self.model}")
#
# # Create an object of the Car class
# my_car1 = Car("BMW", "M5 CS")
# my_car1.display_car()
#
# my_car2= Car("Tata","Punch")
# my_car2.display_car()

# #output:
#
# Car: BMW M5 CS
# Car: Tata Punch


# Calling an Object
# class Calculator:
#     def add(self, x, y):
#         return x + y
#
#     def subtract(self, x, y):
#         return x - y
#
# # Create an object of the Calculator class
# calc = Calculator()
# print(f"Addition: {calc.add(10, 3)}")
# print(f"Subtraction: {calc.subtract(5, 3)}")


# Output:
# Addition: 13
# Subtraction: 2















