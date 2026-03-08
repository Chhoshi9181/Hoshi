import sys
input = sys.stdin.readline

n, m = map(int, input().split())

red = list(map(int, input().split()))
blue = list(map(int, input().split()))

events = []

for x in red:
    events.append((x, 'R'))

for x in blue:
    events.append((x, 'B'))

events.sort()

ans = 1
last = events[0][1]

for i in range(1, len(events)):
    if events[i][1] != last:
        ans += 1
    last = events[i][1]

print(ans)