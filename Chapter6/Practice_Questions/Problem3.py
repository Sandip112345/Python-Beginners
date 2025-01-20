# A spam comment is defined as a text containing following keywords.
# "make a loto of money", "buy now", "Subscribe now", "Click This",
# Write a program to detect these spams
p1, p2, p3, p4 = "make a lot of money", "buy now", "Subscribe now", "Click This"
# print(p1)

message = input("Enter your message: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")