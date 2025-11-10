#Как такого шаблонного решения нет, но есть общий вид решения для этого типа задач

f = open('24.txt').readline().strip()

# Оптимизация: создаем массив префиксных сумм для быстрого подсчета LND
# prefix[i] = количество LND, которые начинаются до позиции i (не включая i)
prefix = [0] * (len(f) + 1)
for i in range(len(f) - 2):
    if f[i:i+3] == 'LND':
        prefix[i+1] = 1

# Преобразуем в префиксные суммы
for i in range(1, len(prefix)):
    prefix[i] += prefix[i-1]

# Функция для O(1) подсчета количества LND в диапазоне [start, end] включительно
# LND начинается на позиции i, значит оно входит, если i >= start и i+2 <= end
# То есть i в диапазоне [start, end-2]
def count_lnd(start, end):
    if end < start + 2:  # LND требует минимум 3 символа
        return 0
    # Количество LND, начинающихся в диапазоне [start, end-2] включительно
    # prefix[i] = количество LND до позиции i (не включая i)
    # Значит prefix[end-1] - prefix[start] = количество LND в [start, end-1)
    # Но нам нужно [start, end-2], что эквивалентно [start, end-1) при end >= start+2
    return prefix[end-1] - prefix[start]

answer = 0  # Максимальная длина последовательности

# Оптимизированный метод двух указателей
# Для каждого start находим максимальный end, где количество LND <= 10000
right = 0
for start in range(len(f)):
    # Расширяем правый указатель от предыдущей позиции (не сбрасываем)
    # Это работает, потому что при увеличении start количество LND может только уменьшиться
    while right < len(f):
        if count_lnd(start, right) > 10000:
            break
        right += 1
    
    # right теперь указывает на первую позицию, где количество LND > 10000
    # Значит, максимальный end = right - 1
    max_end = right - 1
    
    # Проверяем все подстроки [start, end], где f[start] == f[end]
    # Оптимизация: проверяем только те, которые могут быть длиннее текущего максимума
    for end in range(max(start + answer, start), max_end + 1):
        if f[start] == f[end]:
            answer = max(answer, end - start + 1)
    
    # Если right достиг конца, можно выйти раньше
    if right >= len(f):
        # Проверяем оставшиеся подстроки
        for end in range(max(start + answer, start), len(f)):
            if f[start] == f[end] and count_lnd(start, end) <= 10000:
                answer = max(answer, end - start + 1)
        break

print(answer)