#File Handling
#Day4


#Raeding a file
# file=open("mayuresh.txt","r")
# cont=file.read()
# print(cont)

# Output:
# hii how are you
# this is demo file
# using for file programs
# thank you!


#write file
# file=open("write.txt","w")
# file.write("Hii iam write function")
# file.close()
#
# Output:
# Hii iam write function

#append file
# file=open("write.txt","a")
# file.write(" This is added line")
#
# Output:
# Hii iam write function This is added line



#count word occurances
# file=open("mayuresh.txt","r")
# content=file.read()
# words=content.split()
# count=len(words)
# print(f"Total words in file are {count}")

# Output:
# Total words in file are 14



#accepting input from user and apend to file
# file=open("write.txt","a")
# user_input=str(input("Enter String to append to file: "))
# file.write(user_input)
# print("User inpur has been stored in file")


# Output:
# Hii iam write function This is added linehii good morning


#take input from user then read it back

# with open("user_input.txt","w") as file:
#     user_input=input("Enter some input: ")
#     file.write(user_input)
# print("Your Input has been added in file")
# #checking user input that we added in file
#
# with open("user_input.txt","r") as file:
#     user_output=file.read()
#     print("Content of File is \n ")
#     print(user_output)


# Output:
# Enter some input: hii iam mayuresh
# Your Input has been added in file
# Content of File is
# hii iam mayuresh




# Open the file and replace the specific word content
# with open("mayuresh.txt", "r") as file:
#     content = file.read()
#
# # Replace the word
# content = content.replace("mayur", "mayuresh")
#
# # Write the updated content back to the file
# with open("mayuresh.txt", "w") as file:
#     file.write(content)
#
# print("File content has been updated.")


# Output:
# mayuresh
# mayuresh



# file1 = open("myfile.txt", "w")
# L=["hii iam mayuresh \n", "Iam from maharashtra \n", "Iam learning python \n"]
# file1.writelines(L)
# file1.write("hello \n")
# file1.close()


# Output:
# hii iam mayuresh
# Iam from maharashtra
# Iam learning python
# hello


#use writeble() function
#it is use for checking file is writeble or not
# with open("mayuresh.txt","w") as file:
#     if file.writable():
#         print("File is Writeble")
#     else:
#         print("File is not writeble")
#     file.close()

# Output:
# File is Writeble

#Changing file mode w to r

# with open("mayuresh.txt","r") as file:
#     if file.writable():
#         print("File is Writeble")
#     else:
#         print("File is not writeble")
#     file.close()
#
# Output:
# File is not writeble



