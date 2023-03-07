for row in range(5):
    for col in range(5):
        if (col==2 and row>1) or (col==row and row<2) or (row+col==4 and row<2) :
            print("* ",end="")
        else:
            print(end="  ")
    print()