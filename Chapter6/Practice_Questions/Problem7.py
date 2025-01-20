# Write a program to find out whether a given post is talking about "Sandip" or not.

# post = "Hey Sandip brother , how are you do you have some health problem or shomething"

post = input("Enter something about Sandip: ")

name = "Sandip"

if(name.lower() in post.lower()):
    print("This post is talking about Sandip")
else:
    print("This post is not talking about sandip")