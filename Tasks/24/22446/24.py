f = open('24.txt').readline().strip()

answer = 0
count_LND = 0
l = 0

for r in range(2, len(f)):
    if f[r-2:r+1] == 'LND':
        count_LND += 1
    while count_LND > 10000:
        if f[l:l+3] == 'LND':
            count_LND -= 1
        l += 1
    for l1 in range(l, r):
        if f[l1] == f[r]:
            answer = max(answer, r - l1 + 1)
            break
        
print(answer)