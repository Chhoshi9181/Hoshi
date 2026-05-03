s = input().strip()

x, y = 0, 0

for c in s:
    if c == 'N':
        y += 1
    elif c == 'S':
        y -= 1
    elif c == 'E':
        x += 1
    elif c == 'W':
        x -= 1

d = abs(x) + abs(y)

print(x, y, d)