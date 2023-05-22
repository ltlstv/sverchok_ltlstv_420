# Шпора

#include <iostream>
using namespace std;
int main(){
    cin >> x >> y;
    cout << x << y;
    }

>a*b = a * b
>a*a= a^2
>a%b = a - (a/b)

short [−32767, +32767]
unsigned short [0, +65535]

int [−32767, +32767] / [−2 147 483 648, +2 147 483 647]
unsigned int [0, +4 294 967 295]

long [−2 147 483 647, +2 147 483 647]
unsigned long [0, +4 294 967 295]

long long [−9 223 372 036 854 775 808, +9 223 372 036 854 775 807]
unsigned long long [0, 18 446 744 073 709 551 615]

float(32)/double(64)/long double()

>cin >> a;
>cout << char(a);

>char input;
>cin >> input;
>int ia=int(input);
>cout << ia;

char.html - таблица ASCII

перевод из нижнего регистра в верхний: a-32

>char a;
>int i;
>cin >> a >> i; - cчитываем строку посимвольно
>cout << i;

>const double pi = 3.141592653589793;
>double p;
>cin >> p;
>cout.setf(ios::fixed); - ограничивает кол-во чисел после запятой
>cout.precision(p); - устанавливает ограничение размеров в p
>cout << pi;

bool (=0 => 0 иначе 1)