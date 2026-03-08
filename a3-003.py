N = int(input())

r1 = [1] + list(map(int,input().split()))
r2 = [1] + list(map(int,input().split()))

ans = 0

for i in range(N):
    a,b = r1[i], r1[i+1]
    c,d = r2[i], r2[i+1]

    if a==c or a==d or b==c or b==d:
        continue

    if (a-c)*(a-d) < 0 and (b-c)*(b-d) < 0:
        ans += 1

print(ans)