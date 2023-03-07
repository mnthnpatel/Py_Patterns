num = int(input("Enter Number Of Rows :- "))

# 1. Square Printing...

print("Square Shape")
for i in range(num):
    print("* " * (num))
print()


# 2. Right Triangle Printing...

print("Right Triangle Shape")
for i in range(1,num+1):
    print("* " * (i))
print()


#3. Left Triangle Printing...

print("Left Triangle Shape")
for i in range(1,num+1):
    print("  " * (num-i) + "* " * (i))
print()


# 4. Triangle Shape...

print("Triangle Shape")
for i in range(1,num+1):
    print(" " * (num-i) + "* " * (i))
print()


# 5. Diamond Shape...

print("Diamond Shape")
for i in range(1,num+1):
    print(" " * (num-i) + "* " * (i))
for i in range(num-1,0,-1):
    print(" " * (num-i) + "* " * (i))
print()


# 6. Reverse Triangle...
print("Reverse Triangle")
for i in range(num,0,-1):
    print(" " * (num-i) + "* " * (i))
print()


# 7.Reverese Right Triangle...

print("Reverse Right Triangle")
for i in range(num,0,-1):
    print("  " * (num-i) + "* " * (i))
print()


# 8.Reverese Left Triangle...

print("Reverse Left Triangle")
for i in range(num,0,-1):
    print("* " * (i))
print()


# 9.Arrow Pattern...

print("Arrow Pattern")
for i in range(1,num+1):
    print("* " * (i))
for i in range(num-1,0,-1):
    print("* " * (i))


# 10.Reverse Arrow

print("Reverse Arrow")
for i in range(1,num+1):
    print("  " * (num-i) + "* " * (i))
for i in range(num-1,0,-1):
    print("  " * (num-i) + "* " * (i))