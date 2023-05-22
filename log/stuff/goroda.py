from itertools import product 
m=[[0,712,673,1075,875,1622,423],
   [712,0,1385,1800,1577,2348,1128],
   [673,1385,0,1499,239,2046,244],
   [1075,1800,1499,0,1287,551,1266],
   [875,1577,239,1287,0,1835,442],
   [1622,2348,2046,551,1835,0,1813],
   [423,1128,244,1266,422,1813,0]]
wm=0
ways=list(product('0123456', repeat=7))
for x in ways:
    w=0
    #if all(x.count(a)==1 for a in x):
    if len(set(x))==7:
        for n in range(len(x)-1):
            w+=m[int(x[n])][int(x[n+1])]
    if w>wm:
        wm=w
print(wm)
