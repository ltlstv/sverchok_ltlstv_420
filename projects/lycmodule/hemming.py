def hemming():
    a='0123456789'
    nums=list(a)
    print(nums)


    b='0000000 000111 0010110 0011001 0100101 0101010 0110011 0111100 1000011 1001100'
    hem=b.split()
    print(hem)
    for i in range(len(hem)):
      hem[i]=int(hem[i])
    print(hem)


    def distance(x,y):
      k=7
      for i in range(7):
        if x%10==y%10:
          k=k-1
        x=x//10
        y=y//10
      return


    cod=int(input("код="))


    min=distance(cod,hem[0])
    imin=0
    for i in range(10):
      D=distance(cod,hem[i])
      if D<min:
        min=D
        imin=i
      if min==0:
        print(f"Код верный: символ {nums[imin]}")
      elif min==1:
        print(f"Код исправлен: символ {nums[imin]}")
      else:print(f"Код неверный")