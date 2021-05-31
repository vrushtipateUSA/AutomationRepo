n= int(input("enter a value"))
for i in range(n):
    if (i==0):
        print("*", end=" ")
        for j in range(n//2-1):
            print(" ",end=" ")
        for j in range(n//2+1):
            print("*",end=" ")
    elif(i<n//2):
        print("*",end=" ")
        for j in range(n//2-1):
            print(" ", end=" ")
        print("*",end=" ")
    elif(i<n//2):
        for j in range(n):
            print("*", end=" ")
        elif(i<n)
