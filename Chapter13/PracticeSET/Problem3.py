'''3. A list contains the multiplication table of 7.
Write a program to convert it to a vertical string of same 
numbers (7/14)

'''
# table = []
# for i in range(1,11):
#     mul = 7 * i
#     table.append(mul)

table = [str(7*i) for i in range(1,11)]
print(table)
    
verstr = "\n".join(table)
print(verstr)