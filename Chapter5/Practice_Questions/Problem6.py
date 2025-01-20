# Create an empty dict. 
# Allow four friends to enter their favourite language as their values and use keys as their names. 
# Assume that the names are unique.

d = {}

name = input("Enter your name: ")
lang = input("Enter you fav language: ")

d.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter you fav language: ")

d.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter you fav language: ")

d.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter you fav language: ")

d.update({name:lang})


print(d)
print(type(d))