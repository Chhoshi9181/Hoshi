import sys

input = sys.stdin.readline
n = int(input())

points = []
s = set()

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    s.add((x, y))

ans = 0

for i in range(n):
    x1, y1 = points[i]
    for j in range(i+1, n):
        x2, y2 = points[j]

        if abs(x1-x2) == abs(y1-y2):
            if (x1, y2) in s and (x2, y1) in s:
                ans = max(ans, abs(x1-x2))

print(ans)