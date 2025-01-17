Day1
Variables, Data Types, and Basic Operations
#type of variables
x=5
y=34.433
z=("mayur","hii")
a=["mayur","goodmorning"]
print(type(x))
print(type(y))
print(type(z))
print(type(a))
Output:
<class 'int'>
<class 'float'>
<class 'tuple'>
<class 'list'>

Simple arithmetic operations
a = 10
b = 5

print("Addition:", a + b)       # Output: 15
print("Subtraction:", a - b)    # Output: 5
print("Multiplication:", a * b) # Output: 50
print("Division:", a / b)       # Output: 2.0

String concatenation
a = "Hello"
name = str(input("Enter Your Name: "))
print(a + ", " + name + "!")  # Output: Hello, Alice!

output:
Enter Your Name: Mayuresh
Hello, Mayuresh!

Dictionary to store personal details
personal_details = {
    "name": "Mayuresh",
    "age": 23,
    "city": "Shrirampur",
    "pincode":413709,
    "hobbies": ["reading", "cycling", "Travelling"]
                    }

Accessing my personal info
print("Name is",personal_details["name"])
print("Age is",personal_details["age"])

Output:
Name is Mayuresh
Age is 23


Typecasting

String to Tuple
y='mayuresh'
x=tuple(y)
print(type(x))
print(x)

Output:
<class 'tuple'>
('m', 'a', 'y', 'u', 'r', 'e', 's', 'h')



String to Integer
str='200'
num=int(str)
print(type(str))
print(type(num))
print(num)

Output:
<class 'str'>
<class 'int'>
200


Int to Str
int=123
a=str(int)
print(a)
print(type(int))
print(type(a))

Output:
123
<class 'int'>
<class 'str'>



List to Tuple
l1=["Hii","iam","Mayuresh"]
t1=tuple(l1)
print(type(l1))
print(type(t1))
print(t1)


Output:
<class 'list'>
<class 'tuple'>
('Hii', 'iam', 'Mayuresh')







