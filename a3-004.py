import sys

input = sys.stdin.readline

N = int(input())

u = []
v = []

for _ in range(N):
    x,y = map(int,input().split())
    u.append(x+y)
    v.append(x-y)

u.sort()
v.sort()

U = u[N//2]
V = v[N//2]

ans = 0
for i in range(N):
    ans += abs(u[i]-U) + abs(v[i]-V)

print(ans//2)