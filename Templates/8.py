from itertools import * # Импортируем все из модуля itertools для работы с итераторами

alphabet = 'АЛЕЙДОСКП' # Задаем алфавит из букв (!Важно: без повторяющихся букв (обычно) )
alphabet = list(alphabet)
alphabet.sort(reverse=True) # Сортировка по алфавиту в обратном порядке

cnt = 0

nomer = -1 # Номер комбинации (начинается с 0)
for perm in product(alphabet, repeat=6): # Перебираем все возможные комбинации букв длиной 6
    nomer+=1 # Увеличиваем номер комбинации на 1
    word = ''.join(perm) # Преобразуем кортеж в строку
    if nomer % 2 == 0 and (word[:1] == 'К') and (word.count('Й') >= 2) and (word.count('С') == 0) and (word.count('Е') == 0):
        print(nomer)
        break