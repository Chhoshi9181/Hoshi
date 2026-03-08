n, m = map(int, input().split())

red = list(map(int, input().split()))
blue = list(map(int, input().split()))

i = j = 0
last = None
count = 1   # นับจุดเริ่มต้น

while i < n or j < m:
    if j == m or (i < n and red[i] < blue[j]):
        cur = 'r'
        i += 1
    else:
        cur = 'b'
        j += 1
    
    if last is not None and cur != last:
        count += 1
    
    last = cur

print(count)