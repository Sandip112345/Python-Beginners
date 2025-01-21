# Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter your number: "))

for i in range(11):
    print(f"{num} x {i} = {num * i}")

