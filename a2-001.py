import sys
input = sys.stdin.readline

n, m = map(int, input().split())
red = list(map(int, input().split()))
blue = list(map(int, input().split()))

i = 0
j = 0
ans = 1
last = None

while i < n or j < m:

    if j == m or (i < n and red[i] < blue[j]):
        cur = 'R'
        i += 1
    else:
        cur = 'B'
        j += 1

    if last is not None and cur != last:
        ans += 1

    last = cur

print(ans)