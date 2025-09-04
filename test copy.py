for x in range(312614,312651+1):
    k=0
    s=[]
    for y in range(2,x//2+1):
        if x%y==0:
            k+=1
            s.append(y)
            if k>4:
                break
    if k==4:
        print(*s)