'''for a in range(1,1000):
    b = 1
    for x in range(1,1000):
        a1 = x%30!=0
        a2 = x%45==0
        a3 = x%a!=0
        f = a1 or a2 or a3
        if f == 0:
            b = 0
            break
    if b == 1:
        print(a)
        break'''
'''
def f(s,hod):
    if s >=200: return hod%2==0
    if hod == 0: return 0
    com = [f(s+1,hod-1),f(s*3,hod-1)]
    return any(com) if hod%2!=0 else all(com)

for m in range(1,100000):
    if f(m,3)==0:
        print(m)
        break'''
'''
f = open('24 (1).txt').readline()

f = f.replace('AB', '*')
l = f.split('*')

print(max(l, key=len))
'''
'''
def f(x,stop):
    if x > stop: return f(x-2,stop) + f(x//2, stop)
    if x == stop: return 1
    if x < stop: return 0

print(f(31,2))
'''
'''
count=0
sums = []
for x in range(123457,10000000):
    if count==5: break
    for j in range(2,int(x**0.5)+1):

print(sums)
'''

f = open('26_easy_1696618736.txt')
length = 15061
n = 725
l = []
for i in f.readlines():
    l.append(i[:len(i)-1])

l = map(int, l)

l = sorted(l)
resh = []

print(l[:10])

sumar = 0
for elem in l:
    if sumar > length:
        resh.pop()
        break
    if sumar == length:
        break
    resh.append(elem)
    sumar+=int(elem)

time = 0
pay = 0
for task in resh:
    time += task
    pay += time + task

print(len(resh))
print(pay)



















