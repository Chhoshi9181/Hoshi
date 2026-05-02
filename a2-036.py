n, q = map(int, input().split())

cnt = [0] * 1442

for _ in range(n):
    s, e = map(int, input().split())
    cnt[s] += 1
    cnt[e] -= 1

# prefix sum
for i in range(1, 1441):
    cnt[i] += cnt[i-1]

queries = list(map(int, input().split()))

for k in queries:
    print(cnt[k], end=" ")