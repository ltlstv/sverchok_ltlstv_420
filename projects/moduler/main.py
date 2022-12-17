import lycmodule
import gmodule

l=1
while(l!=0):

    n=int(input(print("1) Хемминг\n2) Морзе\n3) Викторина\n4) Генератор имён\n->")))

    for case in gmodule.switch(n):
        if case(1): lycmodule.hemming()
        if case(2): lycmodule.morse()
        if case(3): lycmodule.quektorina()
        if case(4): lycmodule.namegen()
#       choice_bypass = {
#           '1': lycmodule.hemming(),
#           '2': lycmodule.morse(),
#           '3': lycmodule.quektorina(),
#           '4': lycmodule.namegen()
#       }.get(n, 0)

    j  = int(input(print("Повтор?\n->")))
    if j == 1: l=1
    else: l=0