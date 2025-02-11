l = [22, 34, 234, 223]


'''
index = 0
for item in l: 
    print(f"The item number {index} is {item}")
    index += 1
    
    '''

# Above four line code can be simplified using enumerate function


for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}.")

    