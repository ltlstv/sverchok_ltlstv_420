import PySimpleGUI as sg
import webbrowser

sg.theme('SystemDefault')  # Set the theme

s=['1','2','3','4','5','6','7','8','9','12','14','15','16','17','18','19/20/21','22','23','24','25','26','27','пароль', 'анекдот']
a=[
'''
1) определить точки, из которых выходят 3 линии
2) поподставять эти точки и , определить длины линий между ними и увидеть точки соединённые двумя дорогами.
3) поподставять и потом посчитать ответ''',
#1
''' 
from itertools import product
print('x y z w')
nums=product('01',repeat=4)
for i in nums:
    x,y,z,w=i[0],i[1],i[2],i[3]
    if (not(y<=x) or (z<=w) or not(z))==False:
        print(x, y, z, w)''',
#2
'''
1) используем фильтр (раздел данных)
2) далее используем мозг и считаем ответ (иногда нужно скопировать таблицу по значениям и использовать функции)''',
#3
'''
1) расписать 2-ичное древо
2) внести известные данные
3) Соотнести количество вариантов с количеством символов, начиная с минимального кода. ''',
#4
'''
a=bin(79)[2:]
for i in range(2):
    a=a+str((a.count('1')%2))
print(a)''',
#5
'''
from turtle import *
left(90)
for i in range(7):
    forward(300)
    right(120)
pu()
for x in range(1,9):
    for y in range(1,10):
        goto(x*30,y*30)
        dot(2)
done()''',
#6
'''
1) Испольуем формулу V=M*i*t для звука
t - время
i - раширение
m - частота дискретезации
v - объем файла в битах''',
#7
'''
from itertools import product
k=0
n='16 36 56 76 61 63 65 67'
nn=n.split()
nums=product('01234567',repeat=5)
for n in nums:
    numb=''.join(n)
    if numb.count('6')==1 and numb[0]!='0':
        if all(not(x in numb) for x in nn):
            k+=1
---------------------------------------------            
count=0
for a in range (1,8):
    for b in range (8):
        for c in range (8):
            for d in range (8):
                for e in range (8):
                    s=str(a)+str(b)+str(c)+str(d)+str(e)
                    if s.count('6')==1:
                        if s.index('6')==len(s)-1 and int(s[len(s)-2])%2==0:
                            count+=1
                        if s.index('6')==0 and int(s[1])%2==0:
                            count+=1
                        if s.index('6')<len(s)-1 and s.index('6')>0 and int(s[s.index('6')-1])%2==0 and int(s[s.index('6')+1])%2==0:
                            count+=1
print(count)
''',
#8
'''
# загрузка текста из txt
text=t.split(";")
#result = [int(item) for item in text]
result = list(map(int, text))
x=0
y=x+6
counter=double_num=0

while True:
   n=0
   res6=result[x:y]
   for element in res6:
      if res6.count(element)>2:
         for yy in range(res6.count(element)): res6.remove(element) 
         # удаление значений больше 2 штук
      if res6.count(element)==2:
         n+=2   
         double_num=element 
         res6.remove(element)
         res6.remove(element)

   if n==2 and len(res6)==4:  
      if (sum(res6)/len(res6))<=(double_num*2): counter+=1

   print(counter)
   if y>=len(result):break         
   x=x+6
   y=x+6
---------------------------------------------
tt=''66;39;77;31;132;117''
tt=t.split(';')
n=list(map(int,tt))
c=0
for i in range (6400):
    b=i*6
    f=n[b]
    s=n[b+1]
    trd=n[b+2]
    fo=n[b+3]
    fiv=n[b+4]
    six=n[b+5]
    Y=[f,s,trd,fo,fiv,six]
    d=0
    T=False
    diff=0
    sums=0
    for a in range(6): 
       d+=Y.count(Y[a]) 
       if d==8 and a==5:
         T=True
    for p in range(6):
      if Y.count(Y[p])==2:
         sums=2*Y[p]
      if Y.count(Y[p])==1:
         diff+=Y[p]
    diff==diff/4
    if sums>=(diff/4) and diff!=0 and sums!=0 and T:
      c+=1
print(c)   ''',
#9
'''
tt='8'*86
while ('1111'in(tt) or '8888'in(tt)):
    if '1111'in(tt):
        tt = tt.replace('1111','8',1)
    else:
         tt = tt.replace('8888','11',1)
    print(tt)
---------------------------------------------
nums=[2,3,5,7]
for i in range(8,1000):
    flag=True
    for b in range(len(nums)):
        if i%nums[b] == 0:
            flag=False
    if flag:
        nums.append(i)
print(nums)
for n in range(30):
    for i in range(len(nums)):
        if 4*n + 117 ==nums[i]:
            print(n)''',
#12    
'''
tt=3*16**2018-2*8**1028-2**1050-3*4**1100-2022
s=[]
while tt!=0:
    s.append(str(tt%4))
    tt=tt//4

s=''.join(s)
print(s.count('3'))''',
#14
'''
for a in range(0,100):
    if all(((x%3==0) <= (x%5!=0)) or ((x+a)>=70) for x in range(1,10000)):
        print(a)''',
#15
'''
from sys import setrecursionlimit
setrecursionlimit(2030)
def f(x):
    if x==1:
        return 1
    if x>1:
        return x*f(x-1)
print(f(2023)/f(2020))''',
#16
'''
with open('17.txt') as f:
    nums=[int(x) for x in f]
    maxi=[]
    s=[]
   
    for i in range(len(nums)):
      if nums[i]%10==3:
    maximum=0
         maxi.append(nums[i])
    for i in range(len(nums)-1):
        a=abs(nums[i])%10
        b=abs(nums[i+1])%10
        if ((a==3) and (b!=3)) or ((a!=3) and (b==3)):
        if (nums[i]**2+nums[i+1]**2) >= max(maxi)**2: 
            s.append(nums[i]+nums[i+1])
            if nums[i]**2+nums[i+1]**2>maximum:
                maximum=nums[i]**2+nums[i+1]**2
print(len(s), maximum)''',
#17
'''
1) левый верхний угол берём значение из 1 таблицы
2) в ячейке справа складываем значение этой ячейки из таблицы 1 и значения 1 ячейки, аналогично для ячейки снизу
3) далее используем макс()+зн этой ячейки из таблицы 1 (макс() для ячеек сверху с снизу относительно даной)
4) за барьерами используем формулы сложения верхнего и данного значения , аналогично для горизонтального.''',
#18
'''
1) нарисовать двоичное дерево, начиная с победных ходов
2) расписываем дерево на 4 и более хода
3) считаем по усл задачи где чей ход extra (обычно ответ это число, которое можно получить только 1 способом)''',
#19,20,21
'''1) каждому процессу присваиваем цвет
2) закрашиваем клеточки в таблице относительно конца процесса''',
#22
'''
from itertools import product
def f(x,y,z):
    count=0
    for l in range(2,z):
        b=product('12',repeat=l)
        b=list(b)
        for i in b:
            n=x
            if y>10 and i.count('2')>1:
                continue
            for a in range(len(i)):
                if n==17:
                    break
                if i[a]=='1':
                    n+=1
                elif i[a]=='2':
                    n=2
            if n==y:
                count+=1
    return(count)
print(f(1,10,10)f(10,35,25))''',
#23
'''with open('24.txt') as f:
    s=f.readline().replace('C','S').replace('F','S').replace('D','S').replace('A','G').replace('O','G')
    s=s.replace("SG",'*')
    k=0
    kmax=0
    for i in s:
        if i=='*':
            k+=1
            kmax=max(k,kmax)
        else:
            k=0
    print(kmax)''',
#24
'''
for i in range(2023,10**10,2023):
    num=str(i)
    if (num[0]=='1') and (num[2:6]=='2139') and (num[-1]=='4'):
        print(i,i//2023)''',
#25
'''with open('26.txt') as f:
    s=[int(x) for x in f]
    s=sorted(s[1:],reverse=True)
    k,mini=1,s[0]
    for i in range(1,len(s)):
        if s[i]+3<=mini:
            mini=s[i]
            k+=1
    print(k,mini)''',
#26
'''
from itertools import product
def f23(x,y,z):
    count=0
    for i in range(1,z):
        nums=product('12',repeat=i)
        for numb in nums:
            #numb=''.join(n)
            a=x
            if x==10 and numb.count('2')>1:continue
            for ii in numb:
                if a==17: break 
                if ii=='1':a+=1
                elif ii=='2' :a*=2

            if a==y: count+=1
    return count
                
print(f23(1,10,10)*f23(10,35,25))''',
#27
'''
пароль''',

'''
Штирлиц всегда спал как убитый

его даже дважды обводили мелом'''
]
# Define the layout
inp_layout = [[sg.Text('кто по масти?')],      
                 [sg.InputText(key='-IN-')],      
                 [sg.Submit('валяй'), sg.Cancel('ты чё старый')]]   

layout = [
          [sg.Combo(s, default_value=s[0], s=(15,22), enable_events=True, readonly=True, k='-COMBO-', key='Combo'),
          sg.Output(s=(40,10), key='outputt')],
          [sg.Button('трогай', font=('Arial', 12), button_color=('white', '#004e98'), key='process'),
           sg.Button('закрывай', font=('Arial', 12), button_color=('white', '#004e98'), key='button'),
           sg.Button('urls', font=('Arial', 12), button_color=('white', '#004e98'), key='urls'),
           sg.Button('откуда инфа', font=('Arial', 12), button_color=('white', '#004e98'), key='link')]]

# Create the window
window = sg.Window('вопрос брат', inp_layout)    
event, values = window.read()    
window.close()

text_input = values['-IN-']    
sg.popup('зачётно', text_input)

window = sg.Window('егэ шашки', layout)

# Event loop
while True:
    event, values = window.read()

    if event == "link":
        webbrowser.open("https://github.com/ltlstv/sverchok_ltlstv_420")
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    # Exit the app when the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Process the input and update the output when the button is clicked
    if event == 'process':
        choice=a[s.index(values['Combo'])]
        #print(choice)
        window['outputt'].update('')
        window['outputt'].update(choice)
    if event == 'button':
        break
    if event == 'button':
        urls = {
            'Google': 'https://www.google.com', }
        items = sorted(urls.keys())
        sg.theme("SystemDefaultForReal")
        font = ('Courier New', 16, 'underline')

        layout2 = [[sg.Text(txt, tooltip=urls[txt], enable_events=True, font=font,
                           key=f'URL {urls[txt]}')] for txt in items]

        ulr_window = sg.Window('Hyperlink', layout2, size=(250, 150), finalize=True)

        while True:
            event, values = ulr_window.read()
            if event == sg.WINDOW_CLOSED:
                ulr_window.close()
                break
            elif event.startswith("URL "):
                url = event.split(' ')[1]
                webbrowser.open(url)

# Close the window
window.close()
