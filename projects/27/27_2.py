with open("27_2.txt") as f:
    n=int(f.readline())
    s={0:0}
    for i in range(n):
        t=[]
        pair = [int(x) for x in f.readline().split()]
        for elem in pair:
            for value in s.values():
                t.append(elem+value)
        s={z%10:z for z in sorted(t)[::-1]}
        print(s)
    print(max(summ for k,summ in s.items() if k==6))