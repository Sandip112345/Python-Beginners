'''
Write a python function which converts inches to cms.

'''

def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter the inches: "))
print(f"{n} inches equals to {inch_to_cms(n)}")