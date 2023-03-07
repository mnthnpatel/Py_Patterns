num = int(input("Enter Number Of Rows :- "))
for row in range(num,0,-1):
    for col in range(1,row+1):
        print(col,end=" ")
        # print(row,end=" ")      # Print Same Number...
    print()