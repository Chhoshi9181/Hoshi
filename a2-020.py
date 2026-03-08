import sys
import math

input = sys.stdin.readline

N = int(input())
A = [0]*(N+1)

for i in range(1,N+1):
    A[i] = int(input())

visited = [False]*(N+1)

lcm = 1

for i in range(1,N+1):
    if not visited[i]:
        cur = i
        length = 0
        
        while not visited[cur]:
            visited[cur] = True
            cur = A[cur]
            length += 1
        
        lcm = lcm * length // math.gcd(lcm,length)

print(lcm)