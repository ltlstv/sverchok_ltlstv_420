#1
#Ответ 14
#2
#Ответ wzyxu
#3
#Ответ M35
#4
#Ответ 35
#5

b=[0]*1000
for i in range(1000):
    a = bin(i)[2:]+bin(i%4)[2:]
    r=int(a,2)
    n = r-49
    n=max(n,0)
    for x in range(n,min(r,1000)):
        b[x]+=1
print(max(b))


#6

from turtle import *
left(90)
k=20
for i in range(4):
    forward(14*k)
    right(90)
for i in range(5):
    forward(5*k)
    right(45)
penup()
for x in range(20):
    for y in range(20):
        setpos(x*k,y*k)
        dot(3)
done()
#ответ 59

#7

k=1024*768
N=4096
i=12
I=int(k*i*0.8)
z=200*1024*8
print(I/z)
#ответ 5

#8
#Ответ 8200800
#9

count=0
s=open('09.csv').readlines()
for i in range(len(s)):
    m= s[i][:-1].split(',')
    for i in range(len(m)):
        m[i]=int(m[i])  
    if len(set(m))<len(m):
        if m.count(max(m))==1:
            a=0
            for i in m:
                if m.count(i)>1:
                    a+=i
            if max(m)<a:
                count+=1
print(count)

#10
#Ответ 2214
#11
#Ответ 16640
#12
#Ответ 16
#13

from ipaddress import*
for i in range(1,33):
    nn1 = ip_network(f'120.91.176.213/{i}',0)
    nn2 = ip_network(f'120.91.174.205/{i}',0)
    if nn1[0]!=nn2[0]:
        print(i)
        break
print(int('1111000',2))

#14

for x in range(0,40):
    for y in range(0,40):
        a= 5*40**8+7*40**7+x*40**6+6*40**5+9*40**4+2*40**3+y*40**2+40+9
        if a%39==0:
            b = y*40+x
            if int(b**0.5)**2==b:
                print(b)
#ответ 1521

#15

for i in range(0,1000):
    if all((((x & 57>0) or (x & 99>0))<=(x & i >0))==True for x in range(0,1000)):
           print(i)
           break
#ответ123

#16

count=0
def f(n):
    if n==0:
        return 0
    if n>0 and n%2==0:
        return f(n//10)+n%10
    if n%2!=0:
        return f(n//10)
for i in range(10**9,2*10**9):
    if f(i)==0:
        count+=1
print(count)
#ответ 10077696

#17

a = [int(x) for x in open('17.txt')]
b=[]
c = max(x for x in a if str(x)[-3:]=='123')
for i in range(len(a)-2):
    if int(10000<=a[i]<=99999)+int(10000<=a[i+1]<=99999)+int(10000<=a[i+2]<=99999)>=2 and (int(a[i]%3==0)+int(a[i+1]%3==0)+int(a[i+2]%3==0))==1 and sum(a[i:i+3])>c:
        b.append(sum(a[i:i+3]))
print(len(b),max(b))
#ответ 336 253152

#18
#ответ 161 746
#19

def f(x):
    a = [x+1]
    if x%2==0:
        a.append(x+x//2)
    if x%3==0:
        a.append(x+x//3)
    if x%2!=0 and x%3!=0:
        a.append(x*2)
    return a
def g(x):
    if x>=96: return '2'
    if any(a>=96 for a in f(x)):
        return '1'
    if all(g(a)=='1' for a in f(x)):
        return '12'
for i in range(1,96):
    if g(i)=='12':
        print(i)
        break
#ответ 48

#20

from functools import lru_cache
def f(x):
    a = [x+1]
    if x%2==0:
        a.append(x+x//2)
    if x%3==0:
        a.append(x+x//3)
    if x%2!=0 and x%3!=0:
        a.append(x*2)
    return a
@lru_cache(None)
def g(x):
    if x>=96: return '2'
    if any(a>=96 for a in f(x)):
        return '1'
    if all(g(a)=='1' for a in f(x)):
        return '12'
    if any(g(a)=='12' for a in f(x)):
        return '3'
for i in range(1,96):
    if g(i)=='3':
        print(i)
#ответ 57 62
    
#21

from functools import lru_cache
def f(x):
    a = [x+1]
    if x%2==0:
        a.append(x+x//2)
    if x%3==0:
        a.append(x+x//3)
    if x%2!=0 and x%3!=0:
        a.append(x*2)
    return a
@lru_cache(None)
def g(x):
    if x>=96: return '2'
    if any(a>=96 for a in f(x)):
        return '1'
    if all(g(a)=='1' for a in f(x)):
        return '12'
    if any(g(a)=='12' for a in f(x)):
        return '3'
    if all(g(a)=='1' or g(a)=='3' for a in f(x)):
        return '13'
for i in range(1,96):
    if g(i)=='13':
        print(i)
#ответ 56
        
#22
#ответ 73
#23

def f(x,y,z):
    if '11' in z or x>y+2:
        return 0
    if x==y:
        return 1
    else:
        return f(x-1,y,z+'1')+f(x*2,y,z+'2')+f(x*3,y,z+'3')
print(f(3,20,''))           
#ответ 4

#24

s= open('24.txt').readline()
ii=[]
for i in range(len(s)):
    if s[i] in 'AB':
        ii.append(i)
max_l=0
for i in range(len(ii)-5):
    for x in range(2,5):
        r = ii[i]+1
        a = ii[i+x+1]-1
        l=s[r:a+1]
        if l.count('A')<=2 and l.count('B')<=2:
            max_l=max(max_l,len(l))
print(max_l)
#ответ 222

#25

from fnmatch import fnmatch
for i in range(3147,10**10,3147):
    if fnmatch(str(i),'1*4302?1'):
        print(i)
#ответ 100430211
##176430261
##1374430221
##1450430271
##1973430201

#26

s = open('26.txt')
n = int(s.readline())
d=[]
for l in s:
    a,b,c=map(int,l.split())
    d.append([a,b,c])

d.sort()
f=[]
w=[]
j=0
h=0
for a,b,c in d:
    while len(f)>0 and f[0]<=a:
        del f[0]
    while len(w)>0 and w[0]<=a:
        del w[0]
    if c==1 or (c==0 and len(f)<=len(w)):
        if f==[]:
            f.append(a+b)
            j+=1
        elif len(f)<12:
            f.append(f[-1]+b)
            j+=1
        else:
            h+=1
    else:
        if w==[]:
            w.append(a+b)
            
        elif len(w)<12:
            w.append(w[-1]+b)
            
        else:
            h+=1
print(j,h)
#ответ 118 647

#27.A

s=open('27-A.txt')
k = int(s.readline())
k=k*3
n=int(s.readline())
d=[int(x) for x in s]
max_s=0
for i in range(n):
    for x in range(i+1,n):
        for p in range(x+1,n):
            if x-i==k or p-i==k or p-x==k:
                max_s=max(max_s,d[i]+d[x]+d[p])
print(max_s)
#ответ 205323

#27.B
s=open('27-B.txt')
k = int(s.readline())
k=k*3
n=int(s.readline())
d=[int(x) for x in s]
max_s=[[0,0],[0,0],[0,0]]
for i in range(n):
    if d[i]>max_s[0][0]:
        max_s[0]=[d[i],i]
        max_s.sort()
max_f=0
for i in range(n-k):
        if max_s[-1][1]!=i and max_s[-1][1]!=i+k:
            max_f=max(max_f,d[i]+d[i+k]+max_s[-1][0])
        elif max_s[-2][1]!=i and max_s[-2][1]!=i+k:
            max_f=max(max_f,d[i]+d[i+k]+max_s[-2][0])
        else:
            max_f=max(max_f,d[i]+d[i+k]+max_s[-3][0])
print(max_f)
#ответ 20668
