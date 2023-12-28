from math import *
with open("27_1.txt") as f:
    a = [int(x) for x in f] #список, состоящий из всех членов последовательности
d = 19 #делитель
ost=[[] for i in range(d)] #список, создаваемый генератором, где элементом
                            #выступают другие списки; длина списка = 19

for i in a[1:]:
    ost[i%d].append(i)

num=len(ost[0])
rez0=factorial(num)//(factorial(3)*factorial(num-3))
#задаём формулу для рассчёта количество сочетаний num по 3

rez=sum(sorted(ost[0])[-3:])

for i in range(1,len(ost)-2):
    for j in range(i+1,(19-i)//2+1):
        if j!=19-i-j:
            rez=max(rez,max(ost[i])+max(ost[j])+max(ost[19-i-j])) 
            chislas=(f'{i} {j} {19-i-j}')

#ищем максимальную сумму

print(rez0, rez, rez%d, chislas)

#проверяем:
#1) количество сочетаний num по 3 = 4
#2) нужная сумма
#3) нужная сумма кратна 3
#4) остатки, образующие нужную сумму

#      j 19-i-j       i
# 1    │ │            │           19
# ┌────┼─┼────────────┼───────────┐
# └───────────────────────────────┘