print("Enter the numbers for Pattern seperated by comma")
a = input().split(',')
for i in range(len(a)):
    a[i] = int(a[i])
print(max(a))
for row in range(max(a)):
    for column in range(len(a)):
        if row + 1 <= a[column]:
            print('*', sep="", end="")
        else:
            print(" ", sep="", end="")
    print()
