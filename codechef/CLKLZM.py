t = int(input())
for i in range(t):
    (n, m) = (int(x) for x in input().split())
    zmbs = [int(x) for x in input().split()]
    lrk = []
    for j in range(m):
        l, r, k = map(int, input().split())
        lrk.append([l, r, k])
    notdone = True
    bc = 0
    lrk.sort(key = lambda x: x[1] - x[0])
    while(notdone):
        l, r, k = lrk[-1]
        if k == 0 or all(z == 0 for z in zmbs[l-1:r]):
            lrk.pop()
        else:
            for i in range(l-1,r):
                if zmbs[i] > 0: zmbs[i] -= 1
            lrk[-1][-1] -= 1
            bc += 1
        if len(lrk) == 0 or all(z == 0 for z in zmbs) or all(lk[-1]==0 for lk in lrk): notdone = False
    if(all(z==0 for z in zmbs)): print('YES', bc)
    else: print('NO')
