myList = [1, 2, 3, 543, 34]
'''
squaredList = []
for item in myList:
    squaredList.append(item*item)

    '''

squaredList = [i*i for i in myList]

print(squaredList)