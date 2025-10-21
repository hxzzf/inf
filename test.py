from ipaddress import *

ip1 = ip_address("123.20.103.136")
ip2 = ip_address("123.20.103.151")

for mask in range(32,-1,-1):
    net1 = ip_network(f'123.20.103.136/{mask}', 0)
    net2 = ip_network(f'123.20.103.151/{mask}', 0)

    count = 0

    if net1 != net2 and ip1 not in [net1[0],net1[-1]] and ip2 not in [net2[0],net2[-1]]:
        print(mask)
        break

net = ip_network(f'172.16.80.0/255.255.248.0', 0)

count = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('1')%3!=0:
        count+=1

print(count)

st = str(ip1)
mas = list(map(int, st.split('.')))

x = 1
[x:=x*i for i in mas]
print(x)