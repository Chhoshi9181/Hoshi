n = int(input())

fire = water = earth = 0

for _ in range(n):
    F1, W1, E1, F2, W2, E2 = map(int, input().split())
    
    s1 = F1 + W1 + E1
    s2 = F2 + W2 + E2
    
    if s1 >= s2:
        fire += F1
        water += W1
        earth += E1
    else:
        fire += F2
        water += W2
        earth += E2

total = fire + water + earth

print(total)
print(fire, water, earth)

if fire > water + earth:
    print("YES")
else:
    print("NO")