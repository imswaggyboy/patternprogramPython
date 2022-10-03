#Printing Strings in Right Triangle Shape
#without using nested for loop and usign slice
string = input("Enter the string:")
string = string.replace(" ","")
m = len(string)
for triangle in range(1,m+1):
    print(string[:triangle])
    
#using nested for loop
string = input("Enter the string:")
string = string.replace(" ","")
length = len(string)
for row in range(1,length+1):
    for col in range(row):
        print(string[col],end=" ")
    print()
