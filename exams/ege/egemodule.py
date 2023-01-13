def o_five():
    for N in range(516):
        b = f'(N:b)'
        if N % 2 == 0:
            b += '10'
        else:
            b = '1' + b + '01'
        if int(b, 2) > 516:
            print(N)
            break
def o_seven():
    with open('17.txt') as f:    
        numbers=[int(x) for x in f]
        numbers[0]
        print("data(numbers) ->" + numbers)
def tw_four():
    with open('24.txt') as f:
        n=f.readline()
        print("data(n) ->" + n)
def tw_six():
    with open('26.txt') as f:
        data=f.readlines()
        s,n=map(int,data[0].split)
        print("data ->" + data)
def tw_seven():
    data=int(input("data -> "))
    with open('27_B.txt') as f:
        d=f.readlines()
        punkts=d[0]
    for i in range (1,len(d)):
        data.append(d[i].split())
        print("data ->" + data)
def ore_except():
    i=int(input("i -> "))
    num=int(input("num -> "))
    nums=int(input("nums -> "))
    if ((abs(num[i])%10==3) and (abs(num[i+1])%10!=3)) or ((abs(num[i])%10!=3) and (abs(nums[i+1])%10==3)):
        print(True)
def booling():
    x=int(input("x -> "))
    y=int(input("y -> "))
    z=int(input("z -> "))
    a=int(input("a -> "))
    if ((y<=x) or not(z)==False):
        print("if ((y<=x (ИМПЛ)) or(ИЛИ) not(НЕ)(z))==False (ЛОЖЬ):" + " ВЫВОД")
    elif ((y<=x) or not(z)):
        print("if ((y<=x (ИМПЛ)) or(ИЛИ) not(НЕ)(z)) (ИСТИНА):" + " ВЫВОД")
    elif a%14==0:
        print("if a%14==0: a=1 # остаток от деления и проверка на 0")
        a=1
    elif a//14==0:
        print("if a//14==0: a=2 # целая часть от деления и проверка на 0")
def string():
    i = int(input("i -> "))
    num=(bin(i)[2:])
    cou = ("counter -> ")
    print("num(counted) -> " + num.count(cou))
    ind = ("index -> ")
    print("num(indexed) -> " + num.index(ind))
    app = ("appendance -> ")
    print("num(appended) -> " + num.append(app))
    print("num(sorted) -> " + num.sort(reverse=True))  
    print(max(num))
    print(min(num))
    print(sum(num))
