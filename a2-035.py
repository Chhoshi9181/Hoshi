n = int(input())

arr = [input().strip() for _ in range(n)]

used = [False] * n
path = []
count = 0

def dfs():
    global count
    
    if len(path) == n:
        print(" ".join(path))
        count += 1
        return
    
    for i in range(n):
        if not used[i]:
            used[i] = True
            path.append(arr[i])
            
            dfs()
            
            path.pop()
            used[i] = False

dfs()
print(count)