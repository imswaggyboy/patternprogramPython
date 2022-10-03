# hollow right angle shape as per user input 
n= int(input("Enter the number of rows: "))
for row in range(n):
    for col in range(n):
        if row==0 or col==n-1 or (row==col and col>0 and col<n-1):
            print("*",end="")
        else:
            print(end=" ")
    print()



#fixed shape of 5 rows
for row in range(5):
    for col in range(5):
        if row==0 or col==4 or (row==col and col>0 and col<4):
            print("*",end="")
        else:
            print(end=" ")
    print()
