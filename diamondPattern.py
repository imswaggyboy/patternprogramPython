n = int(input("Enter the rows:"))
for i in range(1,n+1):
    print(' '*(n-i)+'* '*(i))
for j in range(n,0,-1):
    print(' '*(n-j+1)+'* '*(j-1))
