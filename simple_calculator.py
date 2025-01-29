def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 'Error: Division by Zero not Allowed'


def calculator():
    print("Welcome to Simple Calculator!!")
    while True:
        print("\nChoose one operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        try:
            choice=int(input("Enter Your Choice:: "))
            if(choice == 5 ):
                print("Exiting the calculator!!!")
                break

            if choice not in [1,2,3,4]:
                print("Invalid Choice !! \n Please Select choice in between 1/2/3/4")
                continue

            x= int(input("Enter First Number:: "))
            y= int(input("Enter Second Number:: "))

            if choice == 1:
                print(f"The Addition of {x} and {y} is {add(x,y)}")

            if choice == 2:
                print(f"The Subtraction of {x} and {y} is {sub(x,y)} ")

            if choice ==3:
                print(f"The Multiplication of {x} and {y} is {mul(x,y)}")

            if choice ==4:
                 print(f"The Multiplication of {x} and {y} is {div(x, y)}")

        except ValueError:
            print("Please Enter valid characters")

        finally:
            print("Thank u for using calculatorrr!! \n Bye!!")


calculator()












