from itertools import product, permutations # Импортируем необходимые функции из модуля itertools

def f(x, y, w, z):
    return (x and (not z)) or (y == z) or (not w) # Определяем логическую функцию f

for x1, x2, x3, x4 in product([0, 1], repeat=4): # Перебираем все комбинации значений для x1, x2, x3, x4
    t = (
        (x1, x2, 0, 0, 0),
        (1, 0, x3, 0, 0), # Добавляем кортежи с различными комбинациями входных значений и ожидаемыми результатами
        (1, 0, 1, x4, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz', r=4): # Перебираем все перестановки переменных 'x', 'y', 'w', 'z'
            if all(f(**dict(zip(p,line))) == line[-1] for line in t): # Проверяем, что функция f возвращает ожидаемые результаты для всех кортежей
                print(*p)
