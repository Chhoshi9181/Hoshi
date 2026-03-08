a = input().strip()
b = input().strip()

# ทำให้ความยาวเท่ากัน
if len(a) < len(b):
    i = 0
    while len(a) < len(b):
        a += a[i]
        i += 1
elif len(b) < len(a):
    i = 0
    while len(b) < len(a):
        b += b[i]
        i += 1

love = "loveLOVE"

res = ""

for x,y in zip(a,b):
    if x in love or y in love:
        res += "w"
    else:
        res += "$"

count_w = res.count("w")

if count_w % 2 == 1:
    mx = 0
    cur = 0
    for c in res:
        if c == "w":
            cur += 1
            mx = max(mx,cur)
        else:
            cur = 0
    res += str(mx)

else:
    if "ww" not in res:
        res += "#"

print(res)