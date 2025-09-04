# IP, для которых сумма единиц в дв записи IP-адреса чётна
from ipaddress import *

def F(ip):
    res=''
    a = str(ip).split('.')
    for s in a:
        res = res + format(int(s), 'b').zfill(8)
    return res

k=0

net = ip_network('192.168.32.160/255.255.255.240', 0)

for ip in net:
    if F(ip).count('1')%2==0:
        k += 1

print(k)

