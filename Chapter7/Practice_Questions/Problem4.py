# Write a program to find whether a given number is prime or not

num = int(input("Enter you number: "))

for i in range(2, num):  # here for num = 2, range becomes (2, 2), since it can't iterrate to goes to for else loop.
    
    if(num%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
    