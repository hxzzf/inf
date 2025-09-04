def F(N):
    st = bin(N)[2:]

    if  N % 2 == 0:
        st = st + '0'
    else:  
        st = st + '1'
    
    return int(st)

for N in range(1, 100):
    if F(N) == 0:
        print(N)
        break
