import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int,input().split()))

X.sort(reverse=True)

energy = 0
drone = 1

for i in range(0, N, 10):
    group = X[i:i+10]

    max_d = group[0]
    others = sum(group[1:])

    energy += drone * (max_d + 2*others)

    drone += 1

print(energy)