N, M = map(int, input().split())

A = [0]*(N+1)
B = [0]*(N+1)

for i in range(1, N+1):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b

targets = list(map(int, input().split()))

ans = []
i = 0

while i < M:
    t = targets[i]

    best = -1
    best_cover = -1

    for j in range(1, N+1):
        if A[j] <= A[t] and B[j] >= B[t]:
            cover = 0
            k = i
            while k < M and A[j] <= A[targets[k]] and B[j] >= B[targets[k]]:
                cover += 1
                k += 1

            if cover > best_cover:
                best_cover = cover
                best = j

    ans.append(best)

    i += best_cover

print(len(ans))
print(*sorted(ans))