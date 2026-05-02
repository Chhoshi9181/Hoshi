from collections import deque

def bpm(u, seen, matchR, graph):
    for v in graph[u]:
        if not seen[v]:
            seen[v] = True
            if matchR[v] == -1 or bpm(matchR[v], seen, matchR, graph):
                matchR[v] = u
                return True
    return False

def can(T, N, K, a1, a2, b1, b2):
    graph = [[] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if a1[i] + b1[j] <= T or a2[i] + b2[j] <= T:
                graph[i].append(j)

    matchR = [-1] * N
    result = 0

    for i in range(N):
        seen = [False] * N
        if bpm(i, seen, matchR, graph):
            result += 1

    return result >= K


# ---- main ----
N, K = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
b1 = list(map(int, input().split()))
b2 = list(map(int, input().split()))

lo, hi = 0, 2_000_000
ans = hi

while lo <= hi:
    mid = (lo + hi) // 2
    if can(mid, N, K, a1, a2, b1, b2):
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(ans)