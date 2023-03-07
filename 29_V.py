for row in range(4):
    for col in range(7):
        if(row==col or row+col==6):
            print("*",end="")
        else:
            print(end=" ")
    print()