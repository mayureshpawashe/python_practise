# Day 2
# Control Flow (If-Else Statements and Loops)
#
#
# if-else
# m=int(input("Enter Your Percentage::"))
# if m > 75:
#     print("First Class")
# elif m <= 75 and m > 50:
#     print("Second Class")
# else:
#     print("Failed")
#
#
# Output:
# Enter Your Percentage::76
# First Class
#
# Enter Your Percentage::67
# Second Class
#
# Enter Your Percentage::30
# Failed
#
#
# nested if
# x=25
# if x > 20:
#     print("Greater than 20")
#
#     if x > 30:
#         print("Greater than 30")
#     else:
#         print("Not Above 30")
#
#
# Output:
# Greater than 20
# Not Above 30
#
#
#
#
# While Loop
# i=1
# while i < 6:
#     print(i)
#     i=i+1
#
# Output:
# 1
# 2
# 3
# 4
# 5
#
#
#
# sum of numbers to limit
# total = 0
# i=1
# n=int(input("Enter The Limit: "))
# while i <= n:
#     total= total + i
#     i=i+1
# print(total)
#
# Output:
# Enter The Limit: 3
# 6
#
#
# Factorial of limit
# num=int(input("enter limit: "))
# fact=1
# i=1
# while i<= num :
#     fact=fact*i
#     i=i+1
# print("Fact is",fact)
#
# Output:
# enter limit: 5
# Fact is 120
#
#
# For Loop
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
#
# Output:
# apple
# banana
# cherry
#
#
#
# student = {"name": "Mayuresh", "age": 23, "marks": 85}
#
# for key, value in student.items():
#     print(key+":",value)
#
# Output:
# name: Mayuresh
# age: 23
# marks: 85
#
#
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end="")
#     print()
#
# Output:
# *
# **
# ***
# ****
# *****
#
#
#
# Break Statement
# for num in range(1,10):
#     if num == 5:
#         break  # breaking the current loop
#     print(num)
#
# Output:
# 1
# 2
# 3
# 4
#
#
#
# continue statement
# for num in range(1,10):
#     if num%2 == 0:
#         continue    #here continue statement skip the even numbers
#     print(num)
#
# Output:
# 1
# 3
# 5
# 7
# 9
#
#
#
# pass statement
# for num in range(1,5):
#     if num == 3:
#         pass    #do nothing when num is 3
#     print(num)
# Output:
# 1
# 2
# 3
# 4
#
#
#
