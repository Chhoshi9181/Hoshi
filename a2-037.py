from collections import deque

q = int(input())

emergency = deque()
normal = deque()

for _ in range(q):
    cmd = input().split()
    
    if cmd[0] == "ARRIVE":
        name = cmd[1]
        typ = cmd[2]
        
        if typ == "emergency":
            emergency.append(name)
        else:
            normal.append(name)
    
    elif cmd[0] == "TREAT":
        if emergency:
            emergency.popleft()
        elif normal:
            normal.popleft()
    
    elif cmd[0] == "SHOW":
        if not emergency and not normal:
            print("EMPTY")
        else:
            print(" ".join(list(emergency) + list(normal)))