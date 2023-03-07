num = int(input("Enter Number Of Rows :- "))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()



# Other Method...

# def pyramid(rows):
#     for i in range(rows):
#         print(' '*(rows-i-1) + '* '*(i+1))
# rows = int(input("Enter Number Of Rows :- "))
# pyramid(rows)