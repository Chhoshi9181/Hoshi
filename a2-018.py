start, n = input().split()
n = int(n)

colors = ["Red", "Green", "Blue"]

index = {'R':0, 'G':1, 'B':2}[start]

for i in range(n):
    print(colors[(index + i) % 3], end=" ")