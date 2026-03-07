n = input()
op = input()

rev = int(n[::-1])
n = int(n)

if op == '+':
    result = n + rev
else:
    result = n * rev

print(n, op, rev, "=", result)