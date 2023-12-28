'''
27 набор данных пары чисел. из пары выбираем одно число, чтобы сумма не делилась на 3 и была максимальной
набираем максимальное и смотрим как добрать разницу, смотря на разницу в апрах чисел и выбирая наименбшие потери
метод частичных сумм
'''
''' 
когда кратко трем, то метод другой - частичные суммы
строится дерево вариантов сумм, чем больше членов, тем сильнее сложность, но писать все не надо,
мы считаем уникальные остатки и выбираем максимальное число
пары
'''
def f1():
    f=['1 3','5 12','6 9','5 4','3 3','1 1']
    #a=[]
    # x,y=map(int,s.split())
    #a+=[(x,y)]
    a=[list(map(int,x.split())) for x in f]
    print(a)

    for x,y in a:
        print(x,y)

    '''частичные суммы'''
    s={0:0}
    for pair in a:
        t=[]
        for elem in pair:
            for value in s.values():
                t.append(elem+value)

        print(f'\n{t}')
        print(sorted(t))
        s={z%3:z for z in sorted(t)} # число не оканчивается на 5 - {z%10:z for z in t} 
        print(s)


    print(max(summ for k,summ in s.items() if k!=0))
#не оканчивается на 5 print(max(summ for k,summ in s.items() if k!=5))
'''макс подстрока'''
#макс и делится на 1000

def f2():
    a=[997,3,4,12,88,1900]
    print(sum(a))
    deletel=1000
    ostatki=[-1]*deletel
    ostatki[0]=0
    summ=raznost=0

    for x in a:
        summ+=x
        ost=summ%deletel
        if ostatki[ost]==-1:
            ostatki[ost]=summ
        elif summ-ostatki[ost]>raznost:
            raznost=summ-ostatki[ost]
            ostt=ostatki[ost]
            s=summ
    print(raznost,s,ostt)
    print(ostatki[:10])
    #2902 все подпоследовательности, где кол-во чисел делящ на 5 кратно 11, количство таких подпосл. 
    '''
    d=11
    pref=[0]*d
    pref[0]=1
    count=0
    for x in a:
    summ+= x%5==0
    ost=summ%deletel
    count+= pref[ost]
    pref[ost]+=1
print(k)
    '''
def f3():#пример
    a=[1,2,3,4,5,6,7,8,9,10]
    s=0
    for i in a:
        s+= i%2==0 
        #if i%2==0:s+=1
    print(s)
def f4():
    #префиксы геолога
    a=[10,-30,40,120,880,-1900]
    s=[0]*len(a)
    delta=2
    for i in range(len(a)):
        s[i]=s[i-1]+a[i]
    mxB=-10**20
    m=10**20
    for i in range(delta+1,len(a)):
        m=min(m,s[i-(delta+1)])
        mxB=max(mxB,s[i],s[i]-m)
    print(mxB)

def f5():
    #подпоследовательность подряд идущих чисел макс суммы и %100=0
    a=[10,30,40,120,880,1900]
    
    ms=0
    s=0
    m=[10**20]*100 # минимальные хвостики
    for x in a:
        s+= x
        if s%100==0:ms=max(ms,s)
        s1=s-m[s%100]#вычитаем минимальный хвост с таким же остатком
        ms=max(ms,s1)
        m[s%100]=min(m[s%100],s)
    print(ms)
def f6():
    # кол-во подпосл сумма эл-ов %67==0
    a=[10,30,40,120,880,1900]
    count=0
    s=0
    hvosty=[0]*67
    for x in a:
        s+=x
        if s%67==0:count+=1
        count+=hvosty[s%67]
        hvosty[s%67]+=1
    print(count)

        
f6()



