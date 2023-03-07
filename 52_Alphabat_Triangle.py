n = int(input("Enter Number Of Rows :- "))
k = ord("A")    # ord Covert Char TO ASCII
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")   # chr Convert ASCII To Char
        k +=1 
    print()



n = int(input("Enter Number Of Rows :- "))
for i in range(n):
    k = ord("A")+i
    for j in range(i+1):
        print(chr(k),end=" ")   # chr Convert ASCII To Char
        k +=1 
    print()