s = input()

count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        print(count, s[i-1], sep="", end="")
        count = 1

print(count, s[-1], sep="")