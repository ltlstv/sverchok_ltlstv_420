N10 = int(input('Ввод: '))
p = 1
while ((p<2) or (p>9)):
    p = int(input('Параметр: '))
k = int(1)
Np = int(0)
while not (N10 == 0):
    Np = Np + (N10 % p)*k
    k = k*10
    N10 = N10 // p
print('N' + str(p) + ' = ' + str(Np))