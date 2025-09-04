import re
s = open('24.txt').readline().strip()
arr = list(re.findall(r'B[1-6]+(?:[*\-][1-6]+)*', s))
print(max([len(x) for x in arr]))
