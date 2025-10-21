import math
m = int(input())
p = int(input())
g = math.gcd(2*m, 2*p)
l = (2*m*2*p)//g//2
print(-1 if (p - m) % g else l)