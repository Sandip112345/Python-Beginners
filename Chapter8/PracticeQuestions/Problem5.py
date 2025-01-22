'''
Write a python function to print first n lines
of following pattern:

'''

def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

# n = int(input("Enter the number : "))
# l = pattern(n)
# print(l)
pattern(3)