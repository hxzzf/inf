from re import *

s = open('24.txt').readline().strip()

num = r'([1-5][0-5]*|0)'

reg = rf'{num}(\*{num})*(-{num})*'

reg = rf'(?=({reg}))'

m = max((x.group(1) for x in finditer(reg, s)), key=len)

print(len(m))