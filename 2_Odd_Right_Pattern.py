num = int(input("Enter Number Of Rows :- "))
k = 1
for i in range(1,num+1):
    for j in range(1,k+1):
        print("*",end=" ")
    k +=2
    print()