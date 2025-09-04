M = [int(x) for x in open('17.txt')]
D = [x for x in M if str(x)[-1] == '3'] # числа, оканчивающиеся на 3
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if str(min(x, y))[-1] == '3':
        if (x ** 2 + y ** 2) < min(D) ** 2:
            R.append(x ** 2 + y ** 2)
print(len(R), max(R))