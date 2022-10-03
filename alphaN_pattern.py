# 'N' shape star pattern
for row in range(7):
    for col in range(7):
        if (col==0) or (col==6) or (col==1 and row==1) or (col==2 and row==2) or (col==3 and row==3) or (col==4 and row==4)  or (col==5 and row==5):
            print("*",end="")
        else:
            print(end=" ")
    print()
#instead of writing this much logical operation we can use our brain to optimize it 
for row in range(6):
    for col in range(6):
        if col==0 or col==5 or (row==col and col>0 and col<5):
            print("*",end="")
        else:
            print(end=" ")
    print()
