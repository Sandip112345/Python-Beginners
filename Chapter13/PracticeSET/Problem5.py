'''5. Write a program to find the maximum of the numbers 
in a list using the reduce function.
'''
from functools import reduce

l = [1,2,34,5,2,345,4,5,34]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))
