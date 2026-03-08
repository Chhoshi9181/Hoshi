s = input()
S = s.upper()

maxu = 0

for i in range(len(S)):
    if S[i] == 'B':
        j = i + 1
        count = 0
        while j < len(S) and S[j] == 'U':
            count += 1
            j += 1
        if count >= 2:
            maxu = max(maxu, count)

if maxu > 0:
    print("Yes", maxu)

elif 'B' in S:
    pos = S.index('B')
    print(s[:pos+1] + 'U'*(len(s)-pos-1))

else:
    pattern = "BUU" * 10
    print(pattern[:len(s)])