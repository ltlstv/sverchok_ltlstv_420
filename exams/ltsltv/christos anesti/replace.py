f = open('24.txt').readline()
a = 'AEIOUY'
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in a:
    f = f.replace(i, str(i) + ' ')

f = f.split()

m=0

print(f[:10])
    
for i in range(len(f)-1):
    spis = []
    c = ''.join(f[i:i+2])[:-1]
    for j in range(0,len(c)):
        for l in range(j+1,len(c)):
            if c[l-1]<c[l]:
                if l==len(c)-1:
                    spis.append(l-j)
                    break
                continue
            spis.append(l-j)
            break
    if spis!=[]:
        m = max(m,max(spis))
        if m == 9:
            print(spis)
            print(c)
            break
print(m)
