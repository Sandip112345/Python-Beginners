# Write a program to greet all the person names stored in a list l1
# and whiich starts with s.
l1 = ["Sandip", "Sagar", "Ramesh", "Suresh"]

for name in l1:
    if(name.startswith("S")):
        print(f"Hello, {name}")