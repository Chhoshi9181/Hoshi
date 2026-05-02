n, m = map(int, input().split())

A = []
for i in range(n):
    l, r = map(int, input().split())
    A.append((l, r, i+1))

need = list(map(int, input().split()))

# เอาเฉพาะถังที่ต้องการ
targets = [A[i-1] for i in need]

# เรียงตามซ้าย
targets.sort()

res = []
i = 0

while i < m:
    l, r, idx = targets[i]

    best_r = r
    best_idx = idx

    j = i
    while j < m and targets[j][0] <= best_r:
        if targets[j][1] > best_r:
            best_r = targets[j][1]
            best_idx = targets[j][2]
        j += 1

    res.append(best_idx)
    i = j

print(len(res))
print(*sorted(res))