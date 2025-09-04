def f(x, y):
    if x > y or x == 30:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)
print(f(2, 12) * f(12, 36))