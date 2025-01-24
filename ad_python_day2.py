# Lambda Functions / Anonymous Functions
# add= lambda a,b: a+b
# print("The Sum is :: ",add(3,5))

# Output:
# The Sum is ::  8


# mul= lambda a,b: a*b
# a=int(input("Enter no1: "))
# b=int(input("Enter no2: "))
# print(f"Multi is :: {mul(a,b)}")

# Output:
# Enter no1: 5
# Enter no2: 4
# Multi is :: 20


# numbers = [1, 2, 3, 4, 5]
# squared_number = list(map(lambda x: x**2, numbers))  #here map is used for iterate the list
# print(squared_number)

# Output: [1, 4, 9, 16, 25]


#add 2 to each number

# num=[11,12,13,14]
# add_num= list(map(lambda x:x+2,num))
# print(add_num)
#
# Output:
# [13, 14, 15, 16]


# Conditional statements
# max numbers

# a= int(input("Enter Number 1:: "))
# b= int(input("Enter Number 2:: "))
# maxx= lambda x,y: x if x>y else y
# print(f"max of two nos is :: {maxx(a,b)}")


# Output:
# Enter Number 1:: 4
# Enter Number 2:: 6
# max of two nos is :: 6


# a= int(input("Enter No:: "))
# oe= lambda x : "Number is Even" if x%2 == 0 else "Number is ODD"
# print(oe(a))

# Output:
# Enter No:: 5
# Number is ODD

# Enter No:: 4
# Number is Even



a= int(input("Enter Number ::"))
check_number = lambda x: "Equal to 10" if x == 10 else "Greater than 10" if x > 10 else "Less than 10"
print(check_number(a))

# Output:
# Enter Number ::12
# Greater than 10

# Enter Number ::10
# Equal to 10







