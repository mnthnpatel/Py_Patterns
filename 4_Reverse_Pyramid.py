num = input("Enter Number Of Rows :- ")
num = int(num)

for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()


# Other Method...
# def reverse(rows):
#     for j in range(rows,0,-1):
#         print(' ' * (rows-j) + '* ' * (j))
# rows = int(input("Enter Number Of Rows :- " ))        
# reverse(rows)