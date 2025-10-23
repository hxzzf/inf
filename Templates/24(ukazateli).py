import re
s = open('24.txt').readline().strip()

mx = 1

for left in range(len(s)):
    for right in range(left + mx + 1, len(s)):
        l = s[left:right]
        if l.count('Y') > 80: break
        if l .count('Y') == 80 and l.count("2025") >= 90:
            mx = max(mx, len(l))

print(mx)