import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

d1 = defaultdict(list)
d2 = defaultdict(list)

for _ in range(n):
    x, y = map(int, input().split())
    d1[x - y].append(x)
    d2[x + y].append(x)

ans = 0

for g in d1.values():
    g.sort()
    if len(g) > 1:
        ans = max(ans, g[-1] - g[0])

for g in d2.values():
    g.sort()
    if len(g) > 1:
        ans = max(ans, g[-1] - g[0])

print(ans)