from re import *

s = open('24.txt').readline().strip()

num = r'([1-9][0-9]*|0)'

reg = rf'{num}([+*]{num})+'

reg = rf'(?=({reg}))'

m = [x.group(1) for x in finditer(reg, s)]

m = sorted(m, key=len)[::-1]

for i in m:
    try:
        if eval(i) == 0:
            print(len(i))
            break
    except:
        continue