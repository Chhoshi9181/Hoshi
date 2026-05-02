s = input().strip().upper()
n = len(s)

# check unknown
if all(c in "IT" for c in s):
    print("unknown", n)
    exit()

i = 0
maxA = 0

while i < n:
    if s[i] == 'R':
        i += 1
        if i >= n or s[i] != 'A':
            print("no", i-1)
            exit()
        cnt = 0
        while i < n and s[i] == 'A':
            cnt += 1
            i += 1
        maxA = max(maxA, cnt)

    elif s[i] == 'B':
        i += 1
        if i >= n or s[i] not in "IT":
            print("no", i-1)
            exit()
        while i < n and s[i] in "IT":
            i += 1

    elif s[i] == 'A':
        # A โผล่เองไม่ได้
        print("no", i)
        exit()

    elif s[i] in "IT":
        i += 1

    else:
        print("no", i)
        exit()

print("yes", maxA)