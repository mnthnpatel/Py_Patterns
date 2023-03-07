num = int(input("Enter Number Of Rows :- "))
for row in range(num):
    for col in range(num):
        if col==row or row==0 or col==num-1:
            print("* ",end="")
        else:
             print(end="  ")
    print()