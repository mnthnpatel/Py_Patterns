
for row in range(5):
    for col in range(5):
        if( row+col==2 or row+col==6 or col-row==2 or row-col==2):
            print("* ",end="")
        else:
            print(end="  ")
    print()


for row in range(7):
    for col in range(7):
        if( row+col==3 or row+col== 9 or col-row==3 or row-col==3):
            print("* ",end="")
        else:
            print(end="  ")
    print()