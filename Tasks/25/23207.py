def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def primes(n):
    for i in range(2, int(n ** 0.5) + 1):
        if (n//i) * i == n and str(i).count('5') == 1 and str(n//i).count('5') == 1 and prime(i) and prime(n//i):
            return i,n//i
    return 0,0
start= 1324728
i = 0
while True:
    if i == 5:
        break
    a,b = primes(start)
    if a != 0 and b != 0:
        print(start, max(a,b))
        i+=1
    start +=1
