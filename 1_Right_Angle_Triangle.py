num = int(input("Enter Number Of Rows :- "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# While Loop...

num = int(input("Enter Number Of Rows :- "))
row=0
while row<num:
    star = row+1
    while star>0:
        print("* ",end="")
        star -=1
    row +=1
    print()