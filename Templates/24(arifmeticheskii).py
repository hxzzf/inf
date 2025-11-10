#Как такого шаблонного решения нет, но есть общий вид решения для этого типа задач

f = open('24.txt').readline().strip()

#Разделяем на фрагменты для удобства работы
f = f.replace('++', ' ')
f = f.replace('**', ' ')
f = f.replace('+*', ' ')
f = f.replace('*+', ' ')
f = f.split()

answer = 0 #Максимальная длина выражения

for fragment in f:
    #Если длина фрамента больше максимальной длины, то пропускаем
    if len(fragment) > answer:
        for l in range(len(fragment)):
            if fragment[l] not in "+*":
                s = '' #Строка для хранения выражения
                for r in range(l, len(fragment)):
                        s += fragment[r] #Собираем выражение
                        # Чтобы не заморачиваться просто обходим любые ошибки
                        try:
                            #Если выражение равно 0 и последний символ не является + или * (т.к. это будет некорректным выражением), то обновляем максимальную длину
                            if eval(s) == 0 and fragment[r] not in '+*':
                                answer = max(answer, len(s))
                        except:
                            continue

print(answer)