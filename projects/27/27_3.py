with open("27_3.txt") as f:
    n = f.readline()
    s=[]
    for i in range(int(n)):
        if i%113==0: s.append(i)
    print(s)