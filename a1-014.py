a = int(input())
b = int(input())
c = int(input())

small = a

if b < small:
    small = b
if c < small:
    small = c

print(small)