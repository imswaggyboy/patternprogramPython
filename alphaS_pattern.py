#'S' shapw star pattern
for row in range(7):
    for col in range(5):
        if ((col==0) and (row==1 or row==2)) or ((col==4) and (row==4 or row==5)) or ((col>0 and col<4) and (row==0 or row==3 or row==6)):
            print("*",end="")
        else: 
            print(end=" ")
    print()
