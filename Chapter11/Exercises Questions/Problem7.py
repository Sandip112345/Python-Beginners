'''
Override the __lens__() method on vector of problem5 to display 
the dimension of vector.
'''



class Vector:
    def __init__(self, l):
        self.l = l


    def __len__(self):
        return len(self.l)
    
#Test the implsemntations
v1 = Vector([1,2,3])

print(len(v1))



