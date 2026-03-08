import sys
input = sys.stdin.readline

N, K = map(int,input().split())

count = [0]*K

for _ in range(N):
    x = int(input())
    count[x-1] += 1

m = min(count)

print(N - m*K)