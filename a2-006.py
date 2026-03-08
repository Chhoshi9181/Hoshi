N = int(input())

grid = [input().strip() for _ in range(N)]

dp = [[False]*N for _ in range(N)]

# เป้าหมาย
dp[N-1][N-1] = (grid[N-1][N-1] == '.')

for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):

        if grid[i][j] == 'X':
            continue

        if i+1 < N and dp[i+1][j]:
            dp[i][j] = True
        if j+1 < N and dp[i][j+1]:
            dp[i][j] = True

count = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == '.' and dp[i][j]:
            count += 1

print(count)