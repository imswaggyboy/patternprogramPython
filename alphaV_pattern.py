# 'V' shape star pattern
for row in range(4):
    for col in range(7):
        if ((col==0 or col==6) and row==0) or ((col==1 or col==5) and row==1) or ((col==2 or col==4) and row==2) or (col==3 and row==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
