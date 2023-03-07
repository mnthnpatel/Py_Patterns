for row in range(4):
    for col in range(7):
        if(col==0 or col==6) or (row+col==3) or ( col==5 and row==2) or (col==4 and row==1):
            print("* ",end="")
        else:
            print(end="  ")
    print()