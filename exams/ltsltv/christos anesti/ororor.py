f = open('24_12476.txt').readline()
while 'ROR' in f or 'ORO' in f: f = f.replace('ORO','OR RO').replace('ROR', 'RO OR')
f = f.split()

for s in f:
    
