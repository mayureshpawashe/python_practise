#Day3
#Functions and Comprehensions

# def greet(name):
#     return "Hello, " + name
#
# print(greet("Mayuresh"))
#
# Output:
# Hello, Mayuresh

# def is_prime(num):
#     if num <= 1:
#         return "Number Is not Prime"
#     for i in range(2, num):
#         if num % i == 0:
#             return "Number Is not Prime"
#     return "Number Is Prime"
# a=int(input("Enter The Number: "))
# print(is_prime(a))

# Output:
# Enter The Number: 13
# Number Is Prime
# Enter The Number: 20
# Number Is not Prime


#Factorial of Number
# def factorial(num):
#     result = 1
#     for i in range(1, num+1):
#         result =result* i
#     return result
# number = int(input("Enter a number: "))
# fact=factorial(number)
# print(f"The factorial of {number} is {fact}")
#
# Output:
# Enter a number: 5
# The factorial of 5 is 120


#check Palimdrome or not function
# def palindrome(number):
#     return num == num[::-1]
# num=str(input("Enter Number or String you want to check: "))
# palindrome(num)
# if palindrome(num):
#     print(f"{num} is Palimdrome")
# else:
#     print(f"{num} is not Palimdrome")

# Output:
# Enter Number or String you want to check: madam
# madam is Palimdrome
# Enter Number or String you want to check: mayur
# mayur is not Palimdrome




#Scope of the variable
# def greet(name, message="Hello"):
#     return f"{message} {name}"
#
# print(greet("Mayuresh"))
# print(greet("Python", "Good morning"))

# Output:
# Hello Mayuresh
# Good morning Python




#Keyword Arguments
# def describe_pet(pet_name, animal_type="dog"):
#     return f"I have a {animal_type} named {pet_name}."
#
# # Positional arguments
# print(describe_pet("Tommy"))
#
# # Keyword arguments
# print(describe_pet(animal_type="cat", pet_name="Kiara"))
#
# Output:
# I have a dog named Tommy.
# I have a cat named Kiara.



#List Comprehension

# nums=[1,2,4,5,6,7,8]
# square=[ i**2 for i in nums]
# print(square)
# even=[ i for i in nums if i % 2 == 0]
# print(even)

# Output:
# [1, 4, 16, 25, 36, 49, 64]
# [2, 4, 6, 8]


# names=["hii","Good","Morning","Mayuresh"]
# new=[ i for i in names if "i" in i]
# print(new)
#
# Output:
# ['hii', 'Morning']

#extract data from list of dictionaries
# students= [
#     {"name":"Mayuresh","Class":"MCS","Marks":99},
#     {"name":"Omkar","Class":"MCS","Marks":80},
#     {"name":"Rahul","Class":"MCS","Marks":40} ]
#
# topper_stud=[i["name"] for i in students if i["Marks"] > 70]
# print(f"List of Tppers :{topper_stud}")
#
# Output:
# List of Tppers :['Mayuresh', 'Omkar']
























