N, M = map(int, input().split())

A = [0]*(N+1)
B = [0]*(N+1)

for i in range(1, N+1):
    A[i], B[i] = map(int, input().split())

targets = list(map(int, input().split()))

cover = [[] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(M):
        t = targets[j]
        if A[i] <= A[t] and B[i] >= B[t]:
            cover[i].append(j)

best_ans = None
best_extra = 10**9

from itertools import combinations

for r in range(1, M+1):
    for comb in combinations(range(1, N+1), r):

        covered = set()
        extra = 0

        for c in comb:
            for j in range(N):
                if A[c] <= A[j+1] and B[c] >= B[j+1]:
                    if j+1 not in targets:
                        extra += 1

            for j in cover[c]:
                covered.add(j)

        if len(covered) == M:
            if best_ans is None or r < len(best_ans) or (r == len(best_ans) and extra < best_extra):
                best_ans = comb
                best_extra = extra

if best_ans is None:
    best_ans = []

print(len(best_ans))
print(*sorted(best_ans))