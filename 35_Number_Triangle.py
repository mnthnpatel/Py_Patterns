num = int(input("Enter Number Of Rows :- "))
i = 1
for row in range(1,num+1):
    for col in range(1,row+1):
        print(i,end=" ")
        i +=1
    print()