import egemodule

while True:
    i = int(input(print("1 - Ex. 12\n2 - Ex. 24\n3 - Ex. 26\n4 - Ex. 27\n -> ")))
    if i == 1: egemodule.o_seven()
    elif i == 2: egemodule.tw_four()
    elif i == 3: egemodule.tw_six()
    elif i == 4: egemodule.tw_seven()
    dcs = int(input(print("Repeat?")))
    if dcs == "NO" or dcs == "no": 
        break