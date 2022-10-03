# Floyd's Triangle | Printing Numbers in Right Triangle Shape
n= int(input("Enter the rows:"))
num = 1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num,end=" ")
        num= num+1
    print()
