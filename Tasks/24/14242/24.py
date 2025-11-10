# Гроб. Перед прочтением надо помолиться

s = open('24.txt').readline()
pref_ch_nch = [0] * (len(s) + 1) #преф. массив чет/нечет
pref_gl_sgl = [0] * (len(s) + 1) #преф. массив гласн/согласн

for i in range(len(s)): #создаем массив преф. чет/нечет и гласн/согласн
    pref_ch_nch[i+1] = pref_ch_nch[i]
    pref_gl_sgl[i+1] = pref_gl_sgl[i]
    if s[i] in 'AE':
        pref_gl_sgl[i+1] += 1
    elif s[i] in 'BD':
        pref_gl_sgl[i+1] -= 1
    elif s[i] in '02':
        pref_ch_nch[i+1] += 1
    elif s[i] in '13':
        pref_ch_nch[i+1] -= 1

combined_arr = list(zip(pref_ch_nch,pref_gl_sgl)) # объединяем 2 массива в 1

first_appear = {}
#словарь 1 вхож. различных вариаций преф. чет/нечет, гл/согл
for i,j in enumerate(combined_arr): 
    first_appear.setdefault(j, i)    #через setdefault установим только 1 вхождение     

last_appear = first_appear.copy()
#словарь послед. вхож. различных вариаций преф. чет/нечет, гл/согл
for i,j in enumerate(combined_arr): #каждый раз перезаписывая знач. в словаре,
    last_appear[j] = i                          #мы получим послед. вхож.
   
dop_arr = [last_appear[i] - first_appear[i] for i in first_appear.keys()]
#массив длин последовательностей с выполненным условием равности (у которых начало=1вхож, конец=посл.вхож)
print(max(dop_arr)) #ответ
