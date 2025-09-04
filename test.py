for x in range(174457,174505+1):
    k=0
    s=[]
    for y in range(2,x//2+1):
        if x%y==0:
            k+=1
            s.append(y)
            if k>2:     # ко-во делителей не учитывая 1 и само число
                break
    if k==2:            # ко-во делителей не учитывая 1 и само число
        print(*s)