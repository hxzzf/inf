def f(s):
    max_len = 0
    n = len(s)
    
    for i in range(n):
        count_R = 0
        count_A = 0
        for j in range(i, n):
            if s[j] == 'R':
                count_R += 1
            elif s[j] == 'A':
                count_A += 1
            
            # Если количество A превысило 3, подстрока больше не подходит
            if count_A > 3:
                break
            
            # Если количество R >= 2, обновляем максимальную длину
            if count_R >= 2:
                max_len = max(max_len, j - i + 1)
    
    return max_len

s = open('24.txt').readline().strip()
print(f(s))