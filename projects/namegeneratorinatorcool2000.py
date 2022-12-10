import random
from typing import Iterable
import time
choice = 1
while choice != 2:
    def main():
        vowels = 'аеёиоуыэюя'
        double_vowels = 'еёяюи'
        consonat = 'бвгджзйклмнпрстфхцчшщъь'
        def z(v):
            for m in v:
                if m == v[-1]:
                    v = v[0:-1]
        def split_(string: str) -> list[str]:
            ans = []
            add = True
            for i, v in enumerate(string):
                v = v.lower()
                if not add:
                    if v in double_vowels and string[i-1] in 'ьъй':
                        ans.append(v)
                    else:
                        ans[-1] += v
                        if test_for(ans[-1], vowels, 1) and i+1 < len(string) and test_for(string[i+1:], vowels, 1) and string[i+1] not in 'ьъ' and i+2 < len(string) and string[i+2] in vowels:
                            add = True
                else:
                    ans.append(v)
                    if test_for(ans[-1], vowels, 1) and i+1 < len(string) and test_for(string[i+1:], vowels, 1) and string[i+1] not in 'ьъ' and i+2 < len(string) and string[i+2] in vowels:
                        add = True
                    else:
                        add = False
            return ans
        def test_for(sub: any,  filt: Iterable, ttype: int) -> bool:
            for i in filt:
                match ttype:
                    case 1:
                        if i in sub:
                            return True
            return False

        gen = input("Введите пол\n1 - Мужской\n2 - Женский\n-> ")
        name = input('Введите имя\n-> ')
        name = split_(name)
        name.reverse()

        name = ''.join(name)

        def end_(name):
            glasn = set("ёуеыаоэяию")
            woman = ["ь", "а", "ия"]
            man = ["им", "ий", "иль", "ей"]
            a = random.randint(0, 3)
            b = random.randint(0, 2)
        

            for i in glasn:
                if i == name[-1]:
                    name = name[0:-1]
                    z(name)

            if gen == 1:
                name = f'{name} + {man[a]}'
            elif gen == 2:
                name = f'{name} + {woman[b]}'


        end_(name)
        print(name)
    a = int(input('Выберите функцию: \n1 - Выполнить программу; \n2 - Вывести справку\n-> '))
    if a == 1:
        main()
        time.sleep(10)
    else:
        print("Работы выполнили:\nГШеф - Толстов Илия\nФронт-разработчик - Соболев Егор\nУволен-Шандриков Виктор\nБэк-разработчик-Шабанова Галина\nТестировали-Шаманина Виктория и Фурсова Анна")
        time.sleep(10)
    choice = int(input("Можем повторить?\n1 - Да\n2 - На сегодня хватит\n-> "))