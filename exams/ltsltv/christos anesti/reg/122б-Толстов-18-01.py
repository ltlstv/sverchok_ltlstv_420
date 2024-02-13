""" import re

eadress = 'ltlstv420@gmail.com'
eadresses = ['ltlstv420@gmail.com', 'il.yatol@mail.ru', 'gfi2k18@gmail.com', 'billgates@yahoo.com']
domain_name_f=set()

name = re.findall('.+(?=@)',eadress)
server_name = re.findall('(?<=@).+',eadress)
server_name_f = re.findall('(@(.*))',eadress)
for elem in eadresses:
    if re.match('.+@(.+).com',elem): domain_name_f.add("".join(re.findall('@(.+).com',str(elem))))
print(name, server_name, server_name_f[0][0], domain_name_f)
 """

""" import re

f = open('24-230.txt').readline()

a = re.findall('(?<=KK)(43\d{2}78\d{3}34)(?=KK)',f)

m = max([x for x in a])
sum_d=1
for digit in m:
    if int(digit)%2!=0: sum_d=sum_d*int(digit)

print(sum_d) """
'''
import re

a = re.findall('((X.X|Y.Y)+)', open('24-197.txt').readline())
print(a[:10])
ans = [line[0] for line in a]
print(len(max(ans,key=len))//3)'''

'''
#9791
import re
file = open('24_9791.txt').readline()

def nonreg(f):
    abc = 'QWRTYUIOPSGHJKLZXVNM'
    for i in abc:
        f = f.replace(i,' ')
    f = f.split()
    print(f[:10])
    print(len(max(f,key=len)))

def reg(f):
    a = re.findall('[0-9A-F]+',f)
    return len(max(a,key=len))

print(reg(file))
'''
'''
#9845
import re
file = open('24_9845.txt').readline()

def nonreg():
    return None

def reg(f):
    a = re.findall('((8|9)?([ABC][89])+(A|B|C)?)',f)
    fix = [line[0] for line in a]
    return len(max(fix, key=len))

print(reg(file))
'''
#demo2024
import re
file = open('24_10105.txt').readline()

def nonreg(f):
    t_pos = [-1] + [k for k,v in enumerate(f) if v=='T'] + [len(f)]

    t100_len = []
    
    for x in zip(t_pos, t_pos[101:]):
        t100_len.append(x[1]-x[0]-1)

    return max(t100_len)
def reg(f):
    a = re.findall('(?=(([^T]*[T]){101}))',f)
    fix = [line[0] for line in a]
    return len(max(fix,key=len))

print(nonreg(file))
print(reg(file))
