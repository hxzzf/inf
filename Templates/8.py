alphabet = ['','','','','','']

count = 0
for x1 in alphabet:
    for x2 in alphabet:
        for x3 in alphabet:
            for x4 in alphabet:
                count += 1
                st = x1 + x2 + x3 + x4

                print(str(count) + '. ' + st)