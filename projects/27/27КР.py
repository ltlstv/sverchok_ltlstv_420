def f1():
    from math import factorial
    with open("27_1.txt") as f:
        a=[int(x) for x in f]
    delitel=19
    ost=[[] for i in range(delitel)]
    
    #print(a[1:])
    for i in a[1:]: 
        ost[i%delitel].append(i)

    print(ost)
    num=len(ost[0])
    rez0=factorial(num)//(factorial(3)*factorial(num-3))
    print(rez0)
    rez=sum(sorted(ost[0])[-3:])
    print(rez)
    print(len(ost))
    for i in range(1,len(ost)-2):
        for j in range(i+1,(19-i)//2+1):
            #print(j,19-i-j)
            if j!=19-i-j:
                print(i,j,19-i-j)
                rez=max(rez,max(ost[i])+max(ost[j])+max(ost[19-i-j]))
                chisla=(f'{i} {j} {19-i-j}')
    print(rez0,rez,rez%delitel,chisla)
def f2():
    with open("27_2.txt") as f:
        b=f.readline()
        a=[list(map(int,x.split())) for x in f]
    s={0:0}
    for pair in a:
        t=[]
        for elem in pair:
            for value in s.values():
                t.append(elem+value)
        s={z%10:z for z in sorted(t)[::-1]}
    print(max(summ for k,summ in s.items() if k==6))

def f3():
    with open("27_3.txt") as f:
        a=[int(x) for x in f]
    #a=[100,300,400,9300,800,500,9500]
    #a=[1,113,0,0,0,0,0,113]
    deletel=113
    ostatki=[10**20]*deletel
    ostatki[0]=0
    summ=raznost=count=lenth=0
    nomera_ost=[10**20]*deletel
    
    for x in a[1:]:
        summ+=x
        count+=1
        ost=summ%deletel
        ostatki[ost]=min(ostatki[ost], summ)
        nomera_ost[ost]=min(nomera_ost[ost],count)
        #if ostatki[ost]==-1:    
        #ostatki[ost]=summ
        #nomera_ost[ost]=count
        raznost=max(raznost,summ-ostatki[ost])
        lenth=max(lenth,count-nomera_ost[ost])
        #if summ-ostatki[ost]>=raznost:
            #raznost=summ-ostatki[ost]
            #lenth=max(lenth,count- nomera_ost[ost])
            
    print(raznost,raznost%113,lenth,count,nomera_ost[ost])

f1()
f2()
f3()