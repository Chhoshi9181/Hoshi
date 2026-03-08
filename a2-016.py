c1, n1 = input().split()
c2, n2 = input().split()

if c1 == c2 and n1 == n2:
    print(1000000)

elif n1 == n2:
    print(100000)

elif n1[-3:] == n2[-3:]:
    if c1 == c2:
        print(2000)
    else:
        print(200)

elif n1[-2:] == n2[-2:]:
    if c1 == c2:
        print(1000)
    else:
        print(100)

elif c1 == c2:
    print(20)

else:
    print(0)