f = open('17 (2).txt')
pairs = []
pairs_mid = []
i = 1
cell = []
m = 0

for line in f.readlines():
    line = line[:len(line)-1]
    if i%2!=0:
        cell.append(line)
    else:
        cell.append(line)
        pairs.append(cell)
        cell = []
    i+=1
    m = max(m, int(line))

i=1
for line in f.readlines():
    line = line[:len(line)-1]
    if i%2==0:
        cell.append(line)
    else:
        cell.append(line)
        pairs_mid.append(cell)
        cell = []
    i+=1

print(pairs[:10])
print(pairs_mid[:10])
for pair in pairs:
    paires = sorted(pair,key=len)
    print(paires)
    if len(paires[0])<3 and len(paires[1])==3 and sum(map(int,pair))>=m:
        print(pair)

for pair in pairs_mid:
    paires = sorted(pair,key=len)
    if len(paires[0])<3 and len(paires[1])==3 and sum(map(int,pair))>=m:
        print(pair)
        
