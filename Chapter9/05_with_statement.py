f = open("file.txt")
print(f.read())
f.close()

# The same can be written using with statement like below:


with open("file.txt") as f:
    print(f.read())

