import random
from typing import Iterable
import time
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
        """subject - Строка для проверки;
        filter_ - Фильтр по которому будет происходить проверка;
        ttype - Может принимать некоторые значения, соответствующие типу проверки
        1 - Если хоть 1 из subject содержится в filter_"""
        for i in filt:
            match ttype:
                case 1:
                    if i in sub:
                        return True
        return False

    gen = input("Введите пол (муж/жен)\n-> ")
    name = input('Введите имя\n-> ')
    name = split_(name)
    name.reverse()

    name = ''.join(name)

    def end_(name):
        glasn = set("ёуеыаоэяию")
        woman = ["ь", "а", "ия"]
        man = ["им", "ий", "иль", "ей"]
        a = random.randint(0, 2)
        b = random.randint(0, 3)

        for i in glasn:
            if i == name[-1]:
                name = name[0:-1]
                z(name)

        if gen == "муж":
            print(name + man[a])
        else:
            print(name + woman[b])



    name = end_(name)
    print(name)
print('Выберите функцию: 1 - Выполнить программу; 2 - Вывести справку')
a = int(input())
if a == 1:
    main()
    time.sleep(10)
else:
    print("Работы выполнили:\nТолстов, Соболев, Шандриков, Фурсова, Шаманина, Шабанова")
    time.sleep(10)