n, m = map(int, input().split())

red = list(map(int, input().split()))
blue = list(map(int, input().split()))

i = j = 0
dir_r = 1
dir_b = 1
ans = 1   # นับจุดเริ่มต้น

while i < n and j < m:
    if red[i] < blue[j]:
        dir_r *= -1
        i += 1
    elif red[i] > blue[j]:
        dir_b *= -1
        j += 1
    else:
        dir_r *= -1
        dir_b *= -1
        i += 1
        j += 1
    
    if dir_r != dir_b:
        ans += 1

print(ans)