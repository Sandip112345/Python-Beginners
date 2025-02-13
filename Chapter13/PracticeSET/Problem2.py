'''2. Write a program to input name , marks and phone number
of a student and format it using the format function like 
below:
"The name of the student is Sandip, his marks are 98 and phone
number is 9865543243"

'''
name = input("Enter your name: ")
marks = input("Enter your marks: ")
phNo = input("Enter Your phone No. : ")

ans = "The name of the student is {}, his marks is {} and phone number is {}".format(name, marks, phNo)
print(ans)