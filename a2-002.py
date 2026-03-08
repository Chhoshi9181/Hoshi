n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

ans = 0

for i in range(n):
    x1, y1 = points[i]
    for j in range(i+1, n):
        x2, y2 = points[j]
        
        if abs(x1-x2) == abs(y1-y2):
            ans = max(ans, abs(x1-x2))

print(ans)