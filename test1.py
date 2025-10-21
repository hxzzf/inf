import turtle as t
from math import *

t.left(90)
t.dot(3, "red")
t.speed(0)
k = 5

for i in range(10+1):
    t.forward(78*k)
    t.right(120)


cnt = 0
t.penup()
for x in range(0, 80):
    for y in range(0, 80):
        f = (x > 0) and (y > tan(radians(30))*x) and (y < tan(radians(150))*x+78)
        if f:
            cnt+=1
print(cnt)
dont()