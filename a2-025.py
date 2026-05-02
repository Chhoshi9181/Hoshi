R, C = map(int, input().split())
sr, sc = map(int, input().split())
N = int(input())

grid = [[0]*C for _ in range(R)]

infected = [tuple(map(int, input().split())) for _ in range(N)]

for r, c in infected:
    for i in range(max(0, r-2), min(R, r+3)):
        for j in range(max(0, c-2), min(C, c+3)):
            d = max(abs(i-r), abs(j-c))
            if d == 0:
                grid[i][j] = max(grid[i][j], 100)
            elif d == 1:
                grid[i][j] = max(grid[i][j], 60)
            elif d == 2:
                grid[i][j] = max(grid[i][j], 20)

# นับ safe
safe = sum(grid[i][j] == 0 for i in range(R) for j in range(C))

print(safe)
print(f"{grid[sr][sc]}%")