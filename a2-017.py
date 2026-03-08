size, type_r = input().split()

price = {
    'S': {'R':60, 'T':80},
    'M': {'R':80, 'T':100},
    'L': {'R':100, 'T':120}
}

total = price[size][type_r]

t = input().split()

if t[0] == 'P':
    total += int(t[1]) * 15
elif t[0] == 'E':
    total += int(t[1]) * 10

print(total)