W, H, M, N = map(int, input().split())

X = list(map(int, input().split()))
Y = list(map(int, input().split()))

# คำนวณความกว้าง
widths = []
prev = 0
for x in X:
    widths.append(x - prev)
    prev = x
widths.append(W - prev)

# คำนวณความสูง
heights = []
prev = 0
for y in Y:
    heights.append(y - prev)
    prev = y
heights.append(H - prev)

areas = []

for w in widths:
    for h in heights:
        areas.append(w * h)

areas.sort(reverse=True)

print(areas[0], areas[1])