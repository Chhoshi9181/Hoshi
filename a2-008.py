import sys
input = sys.stdin.readline

n = int(input())

P = []
V = []

for _ in range(n):
    p, v = map(int, input().split())
    P.append(p)
    V.append(v)

max_v = -1
ans = 0

for i in range(n-1, -1, -1):
    if V[i] < max_v:
        ans += 1
    else:
        max_v = V[i]

print(ans)
