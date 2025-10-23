clA = [[],[]] #Два кластера для данных из файла 27A.txt

for s in open('27A.txt'):
    x,y = [float(d) for d in s.split()]
    if y>10: #Кластер по графику выше Y > 20
        clA[0].append([x,y])
    else:    #Кластер по графику ниже Y ≤ 20
        clA[1].append([x,y])

clB = [[],[],[]] #Три кластера для данных из файла 27B.txt

for s in open('27B.txt'):
    x,y = [float(d) for d in s.split()]
    if y<0 or y>30: #Точки вне области интереса
        pass
    elif x>18: #Кластер по графику правее X > 18
        clB[0].append([x,y])
    elif y<18: #Кластер по графику ниже Y < 18
        clB[1].append([x,y])
    else:      #Кластер по графику в середине
        clB[2].append([x,y])

from math import dist

def centr(cl): #Находит центр кластера как точку с минимальной суммой расстояний до всех остальных точек кластера
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return min(m)[1] #Возвращает точку с минимальной суммой расстояний (индекс 0 - сумма, индекс 1 - точка)

cenA = [centr(cl) for cl in clA] #Находит центры кластеров A
px = min(x for x,y in cenA)
py = min(y for x,y in cenA)
print(int(px*10000), int(py*10000))


cenB = [centr(cl) for cl in clB] #Находит центры кластеров B
q1 = dist(cenB[0], cenB[1])

def max_ras(cl): #Находит максимальное расстояние от центра кластера до точек кластера
    cen = centr(cl)
    return max(dist(cen,p) for p in cl)

q2 = max(max_ras(cl) for cl in clB) #Находит максимальное из максимальных расстояний до центров кластеров B

print(int(q1*10000), int(q2*10000))