import sys
input = sys.stdin.readline

n, m = map(int, input().split())

red = list(map(int, input().split()))
blue = list(map(int, input().split()))

i = j = 0
dir_r = 1
dir_b = 1
ans = 1

while i < n or j < m:

    if j == m or (i < n and red[i] < blue[j]):
        dir_r *= -1
        i += 1

    elif i == n or (j < m and blue[j] < red[i]):
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