n = int(input())

for i in range(1, n+1):
    for j in range(1, i+1):
        if j == 1 or i == n or j == i:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()