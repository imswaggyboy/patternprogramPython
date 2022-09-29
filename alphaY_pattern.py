# 'Y' shape star pattern
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row==0) or ((col==1 or col==3) and row==1) or ((col==2) and (row!=1 and row!= 0)):
            print("*",end="")
        else:
            print(end=" ")
    print(
