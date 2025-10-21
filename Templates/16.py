from functools import lru_cache
@lru_cache(None)

def F(n):
    if n == 10:
        return n
    else:
        return n + F(n - 1)

for n in range(10, 2024):
    F(n)
    
print(F(2024) - F(2022))