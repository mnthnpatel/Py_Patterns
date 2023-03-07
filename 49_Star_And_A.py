from itertools import count


n = int(input("Enter Number Of Rows :- "))
for i in range(n):
    Count = 0
    for j in range(n-i-1):
        print("  ",end="")
    for j in range(i+1):
        print("* ",end="")
        if Count < i:
            print("A ",end="")
            Count+=1
    print()
