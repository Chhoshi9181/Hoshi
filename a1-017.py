y1 = int(input())
m1 = int(input())
d1 = int(input())

y2 = int(input())
m2 = int(input())
d2 = int(input())

if (y1, m1, d1) < (y2, m2, d2):
    print(1)
elif (y1, m1, d1) > (y2, m2, d2):
    print(2)
else:
    print(0)