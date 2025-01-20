n1= int(input("Enter no. 1:"))
n2= int(input("Enter no. 2:"))
n3= int(input("Enter no. 3:"))
n4= int(input("Enter no. 4:"))

if(n1>=n2 and n1>=n3 and n1>=n4):
    if(n1==n2):
        print("n1 and n2 are equal : ", n1)
    elif(n1==n3):
        print("n1 and n3 are equal : ", n1)
    elif(n1==n4):
        print("n1 and n4 are equal : ", n1)
    
    print("Greatest number of them all is n1: ",n1)

elif(n2>=n1 and n2>=n3 and n2>=n4):
    if(n1==n2):
        print("n1 and n2 are equal : ", n2)
    elif(n2==n3):
        print("n2 and n3 are equal : ", n2)
    elif(n2==n4):
        print("n2 and n4 are equal : ", n2)

    print("Greatest number of them all is n2: ", n2)

elif(n3>=n1 and n3>=n2 and n3>=n4):
    if(n3==n1):
        print("n1 and n3 are equal : ", n3)
    elif(n3==n2):
        print("n2 and n3 are equal : ", n3)
    elif(n3==n4):
        print("n3 and n4 are equal : ", n3)
    print("Greatest number of them all is n4: ", n3)

elif(n4>=n1 and n4>=n3 and n4>=n2):
    if(n4==n1):
        print("n1 and n4 are equal : ", n4)
    elif(n4==n2):
        print("n4 and n2 are equal : ", n4)
    elif(n4==n3):
        print("n3 and n4 are equal : ", n4)


    print("Greatest number of them all is n4: ", n4)

else:
    print(f"All are equal:  {n1},{n2}, {n3} and {n4}")
