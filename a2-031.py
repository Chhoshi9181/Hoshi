n = int(input())

dna1 = input().split()
dna2 = input().split()

m = int(input())

# ทำการเปลี่ยนยีน
for _ in range(m):
    strand, pos, gene = input().split()
    strand = int(strand)
    pos = int(pos)
    
    if strand == 1:
        dna1[pos] = gene
    else:
        dna2[pos] = gene

# แสดงผล DNA หลังเปลี่ยน
print(" ".join(dna1))
print(" ".join(dna2))

# ตรวจคู่
wrong = 0

for i in range(n):
    a = dna1[i]
    b = dna2[i]
    
    if not ((a == 'A' and b == 'T') or
            (a == 'T' and b == 'A') or
            (a == 'C' and b == 'G') or
            (a == 'G' and b == 'C')):
        wrong += 1

print(wrong)