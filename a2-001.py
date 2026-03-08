import sys
input = sys.stdin.readline

n, m = map(int, input().split())

red = [int(input()) for _ in range(n)]
blue = [int(input()) for _ in range(m)]

i = j = 0
count = 0
last = None

while i < n or j < m:

    if j == m or (i < n and red[i] < blue[j]):
        cur = 'R'
        i += 1
    else:
        cur = 'B'
        j += 1

    if last is not None and cur != last:
        count += 1

    last = cur

print(count + 1)