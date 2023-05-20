from itertools import product
a = [[],
      [712],
      [673,1385],
      [1075,1800,1499],
      [875,1577,239,1287],
      [1622,2348,2046,551,1835],
      [423,1128,244,1266,442,1813]]
b='0123456'
c = product(b,repeat=7)
maxx=0
for i in c:
    if all(i.count(x)==1 for x in b):
        s=0
        for l in range(len(i)-1):
            if i[l]>i[l+1]:
                s+=a[int(i[l])][int(i[l+1])]
            else:
                s+=a[int(i[l+1])][int(i[l])]
            if s>=maxx:
                maxx=s
print(maxx)