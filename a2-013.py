boba, g = input().split()
g = int(g)

tea, sweet, cc = input().split()
sweet = int(sweet)
cc = int(cc)

boba_energy = {'H':5, 'O':3, 'J':2}

tea_energy = {
    'R':[12,18,25],
    'T':[15,20,30],
    'M':[10,15,20]
}

total = boba_energy[boba]*g + tea_energy[tea][sweet-1]*cc

print(total)