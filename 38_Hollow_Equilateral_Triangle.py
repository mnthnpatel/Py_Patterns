num = int(input("Enter Number Of Rows :- "))
for row in range(1,num+1):
    for col in range(1,2*num):
        if row==num or (col+row==num+1) or (col-row==num-1):
            print("* ",end="")
        else:
            print(end="  ")
    print()


num = int(input("Enter Number Of Rows :- "))
k = 2
for row in range(1,num+1):
    for col in range(1,2*num):
        
        if (col+row==num+1) or (col-row==num-1):
            print("* ",end="")

        elif row==num and col!=k:
            print("* ",end="")
            k +=2

        else:
            print(end="  ")
    print()