def f(s1,s2, m):
    if s1 + s2 >= 82:
        return m % 2 == 0
    if m == 0:
        return 0
    moves = [
        f(s1 + 1, s2,m-1),
        f(s1 * 4, s2,m-1),
        f(s1, s2 + 1,m-1),
        f(s1, s2 * 4,m-1)
    ]
    return any(moves) if m % 2 else any(moves) # при поиске неудачного кода заменить на any(moves)
    
    
for s in range(1, 77):
    if not f(4,s,1) and f(4,s,2):
        print(s)