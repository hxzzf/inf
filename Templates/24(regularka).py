from re import *

s = open('24.txt').readline().strip()

num = r'([1-9][0-9]*|0)' # числа без ведущих нулей

reg = rf'{num}([+*]{num})+' # выражения, состоящие из чисел и операций + и *

reg = rf'(?=({reg}))'

m = [x.group(1) for x in finditer(reg, s)]

m = sorted(m, key=len)[::-1] # сортируем по убыванию длины

for i in m:
    try:
        if eval(i) == 0: # проверяем значение выражения
            print(len(i))
            break
    except:
        continue