#Exception Handling in Python


# try:
#     num = int(input("Enter a number: "))
#     print(f"You entered {num}")
# except ValueError:
#     print("That's not a valid number!")
# finally:
#     print("Hii iam Finally block and iam always executed!!")
#
#
# Output:
# Enter a number: 123
# You entered 123
# Hii iam Finally block and iam always executed!!


# num= int(input("Enter Numerator :: "))
# deno= int(input("Enter Denominator:: "))
# try:
#     result= num/deno
#     print(f"The division is :: {result}")
#
# except ZeroDivisionError:
#     print("Error: Divisible by Zero is Not Possible!!")


# Output:
# Enter Numerator :: 12
# Enter Denominator:: 123
# The division is :: 0.0975609756097561

# Enter Numerator :: 10
# Enter Denominator:: 0
# Error: Divisible by Zero is Not Possible!!

# File Handle with Exception


# try:
#     file_name = input("Enter File Name: ")
#     with open(file_name,"r") as file:
#         print("File Content: \n")
#         print(file.read())
# except FileNotFoundError:
#     print("File Not Found !!!")
#
# except PermissionError:
#     print("You Do not Have Permission to Read !!!")
#
# except Exception as e:
#     print(f"Unexcepted Error Occured{e}")
# finally:
#     print("File Operation Completed")


# Output:
# Enter File Name: mayu
# File Not Found !!!
# File Operation Completed


# Output:
# Enter File Name: write.txt
# File Content:
#
# Hii iam write function This is added linehii good morning
# File Operation Completed


# by trying to access an index of a string that may be out of range.
# str="python is simple"
# index=int(input("Enter Index :: "))
# try:
#     char=str[index]
#     print(f"The Chracter at index {index} is : {char}")
# except IndexError:
#     print("Error : Index Out of Range")


# Output:
# Enter Index :: 5
# The Chracter at index 5 is : n

# Enter Index :: 44
# Error : Index Out of Range


#Implement small login system project using try catch

# user_details = {
#     "mayur": "admin123"
# }
#
# try:
#     username = input("Enter Username:: ")
#     password = input("Enter Password:: ")
#
#     # Check if username exists
#     if username not in user_details:
#         raise KeyError("Username Not Found")
#
#     # Check if the password matches
#     if user_details[username] != password:
#         raise ValueError("Incorrect Password")
#
#     print("Login Successful!!!!")
#
# except KeyError as e:
#     print(f"Error:: {e}")
# except ValueError as e:
#     print(f"Error:: {e}")
#
# finally:
#     print("Login attempt is completed")


# Output:
# Enter Username:: mayurr
# Enter Password:: admin123
# Error:: 'Username Not Found'
# Login attempt is completed

# Enter Username:: mayur
# Enter Password:: admin1234
# Error:: Incorrect Password
# Login attempt is completed
