# Перед питоном нужно открыть файл в LibreOffice и сохранить его как CSV с разделителем ; (точка с запятой)

f = open("9.csv").readlines() # чтение файла

cnt = 0

for line in f:
    mas = line.strip().split(';') # разбивка строки по символу ;
    
    mas = list(map(int, mas)) # преобразование элементов строки в целые числа и пихание их в массив

    flag1 = (len(set(mas)) == len(mas))
    
    if flag1:
        if 2*(max(mas)+min(mas)) >= sum(map(int, mas))-max(mas)-min(mas):
            cnt+=1

print(cnt)