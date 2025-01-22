'''Write a python function to print
 multiplication table of a given number

'''

def multiply(n):
    for i in range(1, 11):
        if(len(str(n * i))<2):
            print(f"{n} x {i} = 0{n * i}")
        elif(len(str(n))==2):
            print(f"{n} x {i} = 0{n * i}")
        else:   
            print(f"{n} x {i} = {n * i}")
    
num = int(input("Enter a number: "))
multiply(num)
num = int(input("Enter a number: "))
multiply(num)


