'''
Write a porgram to open three files 1.txt, 2.txt, and 3.txt. If 
any of these files are not present, a message without
exiting the progra must be printed prompting
the same.
'''
try:

    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:

    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:

    with open("3.txt", "w") as f:
        print(f.read())
except Exception as e:
    print(e)
