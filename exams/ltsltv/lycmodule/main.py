import hemming
import morse

a=int(input(print("1 - Хемминг\n2 - Морзе\n")))
if a == 1:
    hemming.hemming()
elif a == 2:
    morse.morse()
