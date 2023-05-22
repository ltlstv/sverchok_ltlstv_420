import math 
def perevod(a,b):
    if b== "байт":
        a=a*2**3
    elif b== "килобайт":
        a=a*2**13
    elif b== "мегабайт":
        a=a*2**23
    elif b== "гигабайт":
        a=a*2**33
    return a 
def it(N):
    T = int(math.log2(2*N-1))
    return T
def pamyat():
    N ="1 - Мощность алфавита(N), "
    K ="2 - колво символов в тексте(K), "
    I ="3 - инф объём текста(I), "
    i ="0 - инф  символа(i), "
    print("что нужно найти? (",i,N,K,I,")")
    G=input()
    if G=="0":
        N=(input("N-&\n"))
        K=int(input("K-&\n"))
        I,V=int(input("I-&\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if N=="":
            print(K*perevod(I,V))
        else: 
            print(it(int(N)))
    if G=="1":
        i=int(input("i-?\n"))
        print(2**i)
    if G=="3":
        K=int(input("K-?\n"))
        N=int(input("N-?\n"))
        i,V=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if i=="":
             I=it(N)*K
        else:
            I=perevod(int(i),V)*K
        print(I)
    if G=="2":
        I,V1=int(input("I-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        i,V2=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        N=int(input("N-?\n"))
        if i=="":
            K=perevod(I,V1)/it(N)
        else:
            K=perevod(I,V1)/perevod(int(i),V2)
        print(K)
def zvuk():
    N ="0 - количество уровней сигнала(N), "
    D ="1 - частота дискретизации(D), "
    V ="2 - объём звуковоо файла(V), "
    i ="3 - глубина звука(i), "
    T ="4 - длительность звукового файла"
    print("Что нужно найти? (",N,D,V,i,T,")")
    G=input()
    if G=="0":
        i,b=int(input("i-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        print(2**perevod(i,b))
    if G=="1":
        N=int(input("N-?\n"))
        i,b1=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        T=int(input("T-?\n"))
        V,b2=int(input("V-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if i =="":
            print(perevod(V,b2)/(it(N)*T))
        else:
            print(perevod(V,b2)/(perevod(i,b1)*T))
    if G=="2":
        D=int(input("D-?\n"))
        i,b1=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        N=int(input("N-?\n"))
        T=int(input("T-?\n"))
        if i =="":
            print(D*(it(N)*T))
        else:
            print(D*(perevod(i,b1)*T))
    if G=="3":
        N=int(input("N-?\n"))
        T=int(input("T-?\n"))
        V,b2=int(input("V-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        D=int(input("D-?\n"))
        if N=="":
            print(perevod(V,b2)/(D*T))
        else:
            print(it(N))
    if G=="4":
        N=int(input("N-?\n"))
        i,b1=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        V,b2=int(input("V-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        D=int(input("D-?\n"))
        if i =="":
            print(perevod(V,b2)/(perevod(i,b1)*D))
        else:
            print(perevod(V,b2)/(it(N)*D))
def isobr():
    N ="0 - количество цветов в политре(N), "
    H ="1 - высота изображения(H), "
    W ="2 - ширина изображения(W), "
    i ="3 - глубина текста(i), "
    I ="4 - инф объём изображения(I), "
    print("Что нужно найти? (",N,i,H,W,")")
    G=input()
    if G=="0":
        i,b1=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        print(2**perevod(i,b1))
    if G=="1":
        i,b1=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        N=int(input("N-?\n"))
        W=int(input("W-?\n"))
        I,b2=int(input("I-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if i=="":
            print(perevod(I,b2)/(it(N)*W))
        else:
            print(perevod(I,b2)/(perevod(i,b1)*W))
    if G=="2":
        i,b1=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        N=int(input("N-?\n"))
        H=int(input("H-?\n"))
        I,b2=int(input("I-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if i=="":
            print(perevod(I,b2)/(it(N)*H))
        else:
            print(perevod(I,b2)/(perevod(i,b1)*H))
    if G=="3":
        N=int(input("N-?\n"))
        W=int(input("W-?\n"))
        I,b2=int(input("I-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        N=int(input("N-?\n"))
        if N=="":
            print(perevod(I,b2)/(H*W))
        else:
            print(it(N))
    if G=="4":
        N=int(input("N-?\n"))
        N=int(input("N-?\n"))
        W=int(input("W-?\n"))
        i,b1=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if i =="":
            print(W*(it(N)*H))
        else:
            print(W*(perevod(i,b1)*H))
print("Какой тип задачи нужно решить? (звук, инфа, изобр)")
A=input()
if A=="звук":
    zvuk()
if A=="инфа":
    pamyat()
if A=="изобр":
    isobr()
