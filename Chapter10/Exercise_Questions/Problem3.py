'''
Create a class wth a class attribute a;
Create an object from it and set a directly
using object. a = 0. Does this change the class attribute?


'''

class Demo:
    a = 4

o = Demo()
o.a = 0

print(o.a)
print(Demo.a)