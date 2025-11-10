f = open('24.txt').readline().strip()

f = f.replace('++', ' ')
f = f.replace('**', ' ')
f = f.replace('+*', ' ')
f = f.replace('*+', ' ')
f = f.split()

answer = 0
for fragment in f:
    if len(fragment) > answer:
        for l in range(len(fragment)):
            if fragment[l] not in "+*":
                s = ''
                for r in range(l, len(fragment)):
                        s += fragment[r]
                        try:
                            if eval(s) == 0 and fragment[r] not in '+*':
                                answer = max(answer, len(s))
                        except:
                            continue

print(answer)