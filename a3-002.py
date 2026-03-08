from collections import deque
import math

N = int(input())

def row_of(x):
    return math.ceil((math.sqrt(8*x+1)-1)/2)

def num(r,c):
    return r*(r-1)//2 + c

visited = set()
q = deque([(N,0)])

while q:
    x,d = q.popleft()
    
    if x == 1:
        print(d)
        break
    
    if x in visited:
        continue
    visited.add(x)
    
    r = row_of(x)
    c = x - r*(r-1)//2
    
    neighbors = [
        (r,c-1),(r,c+1),
        (r-1,c-1),(r-1,c),
        (r+1,c),(r+1,c+1)
    ]
    
    for nr,nc in neighbors:
        if nr>=1 and 1<=nc<=nr:
            y = num(nr,nc)
            if y>=1 and y not in visited:
                q.append((y,d+1))