L, N = map(int, input().split())

bridges = []
for _ in range(N):
    a, b = map(int, input().split())
    bridges.append((a, b))

ans = 0

for i in range(L):
    x = i + 0.5
    count = 0
    
    for a, b in bridges:
        if a < x < b:
            count += 1
    
    ans = max(ans, count)

print(ans)