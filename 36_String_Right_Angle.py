# word = input("Enter Any Word :- ")
# length = len(word)
# for row in range(length):
#     for col in range(row+1):
#         print(word[col],end=" ")
#     print()

# Another Method...
str = input("Enter Any String :- ")
x = 0
for i in str:
    x +=1
    print(str[0:x])