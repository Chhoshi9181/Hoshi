import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())

A = [0]*(N+1)
L = [0]*(N+1)
B = [0]*(N+1)
R = [0]*(N+1)

for i in range(1, N+1):
    A[i], L[i], B[i], R[i] = map(int, input().split())

ans = 0

def solve(i):
    global ans

    if A[i] == 1:
        left = L[i]
    else:
        left = solve(L[i])

    if B[i] == 1:
        right = R[i]
    else:
        right = solve(R[i])

    if left > right:
        ans += left - right
        right = left
    else:
        ans += right - left
        left = right

    return left + right

solve(1)

print(ans)