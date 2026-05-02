def build_segments(arr):
    segs = []
    y = 1  # เริ่มด้านบน (หรือจะเริ่ม 0 ก็ได้ แต่ต้องเหมือนกันทั้งสองเส้น)
    for i in range(len(arr) - 1):
        x1, x2 = arr[i], arr[i+1]
        segs.append((x1, y, x2, 1 - y))
        y = 1 - y
    return segs


def intersect(s1, s2):
    x1, y1, x2, y2 = s1
    x3, y3, x4, y4 = s2

    # เช็คช่วง x ทับกันไหม
    l = max(min(x1, x2), min(x3, x4))
    r = min(max(x1, x2), max(x3, x4))
    if l >= r:
        return False

    # ใช้ cross product
    def ccw(ax, ay, bx, by, cx, cy):
        return (bx - ax)*(cy - ay) - (by - ay)*(cx - ax)

    return (ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4) < 0 and
            ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2) < 0)


# ---------- main ----------
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

segA = build_segments(A)
segB = build_segments(B)

count = 0
for a in segA:
    for b in segB:
        if intersect(a, b):
            count += 1

print(count)