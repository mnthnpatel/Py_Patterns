num = int(input("Enter Number Of Rows :- "))
for row in range(num):
    val = row+1
    dec = num-1
    for col in range(row+1):
        print(format(val,"<3"),end=" ")
        val = val+dec
        dec -=1
    print()