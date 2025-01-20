a = ()  # a is tuple
b = (4) # b is not a tuple but an integers, because for single tuple the number should be followed by a comma
c = (5,) # c is single tuple denoted by comma
d = (1, 45, 342, True, "Python is best!")
e = ("Python is best!")     # e is not a single tuple as b and is strings for the same reason as for "b"

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))