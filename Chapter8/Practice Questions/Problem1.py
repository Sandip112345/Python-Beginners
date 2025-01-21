'''
Write a program using function to find greatest of three numbers 
'''


def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return c
    elif(c>a and c>b):
        return c

a = int(input("Enter first num: "))
b = int(input("Enter second num: "))
c = int(input("Enter third num: "))

print(greatest(a, b, c))