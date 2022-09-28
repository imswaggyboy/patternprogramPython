num = int(input("Enter the rows:"))
for i in range(1,num+1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
