n = int(input())

count = [0]*301

for _ in range(n):
    x = int(input())
    count[x] += 1

print(max(count))