n = int(input())

count = 0
max_weight = -1
max_name = ""

for _ in range(n):
    name, w = input().split()
    w = int(w)

    if w > 15:
        count += 1

    if w > max_weight:
        max_weight = w
        max_name = name

print(count)
print(max_name, max_weight)