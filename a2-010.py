import sys
input = sys.stdin.readline

N,Q = map(int,input().split())

depth=[]
cur=0

for _ in range(N):
    D,L = map(int,input().split())
    for _ in range(L):
        cur+=D
        depth.append(cur)

n=len(depth)

stack=[]
best=[0]*(n+1)

for i in range(n+1):
    h = depth[i] if i<n else 0
    start=i
    
    while stack and stack[-1][1] > h:
        idx,height = stack.pop()
        width = i-idx
        best[width]=max(best[width],height)
        start=idx
    
    stack.append((start,h))

for i in range(n-1,0,-1):
    best[i]=max(best[i],best[i+1])

for _ in range(Q):
    w=int(input())
    if w>n:
        print(0)
    else:
        print(best[w])