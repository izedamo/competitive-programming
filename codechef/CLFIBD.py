t = int(input().strip())
strs = []
for i in range(t):
    strs.append(input().strip())
for s in strs:
    sset = set(s)
    if len(sset) < 3: print('Dynamic')
    else:
        sct = []
        for c in sset:
            sct.append(s.count(c))
        sct.sort()
    if sct[-1] == sct[-2] + sct[-3]: print('Dynamic')
    else: print('Not')
