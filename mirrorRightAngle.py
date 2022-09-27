num = int(input("Enter the rows:"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(" ",end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()
