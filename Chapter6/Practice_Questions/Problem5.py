# Write a program which finds out whether a given username consists less than 10 characters or not

username = input("Enter username")

if(len(username)<10):
    print("Your username contains less that 10 character")
else:
    print("All is well.")