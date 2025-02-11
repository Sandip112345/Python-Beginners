a = int(input("Ener a number: "))
b = int(input("Ener a number: "))
c = int(input("Ener a number: "))

if(b==0):
    raise ZeroDivisionError("Hey our program is not meant to divede numbers by zero")

else:
    print(f"The division a/b is {a/b}")