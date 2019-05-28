# finish zombies one by one, use greedy approach and difference array.

#import heapq
#TODO: difference array, heapq

from sys import stdin
from itertools import accumulate as ac
#import numpy as np

t = int(stdin.readline())
for i in range(t):
    (n, m) = (int(x) for x in stdin.readline().split())
    zmbs = [int(x) for x in stdin.readline().split()]
    lrk = []
    for j in range(m):
        l, r, k = map(int, stdin.readline().split())
        lrk.append([l, r, k])
    d = [z[i]-z[i-1] for i in range(1, len(zmbs))] # difference array
    #d = np.diff(zmbs)
    d.insert(0, z[0])
    u = []
    ans = 0
    failed = False
    #zkilled = 0
    for zi in range(n):
        u += [x for x in lrk if x[0] == zi+1]
        u.sort(key=lambda x: x[1])
        #z = zmbs[zi]
        while(zmbs[zi] > 0):
            if u == [] or u[-1][1] < zi+1:
                # zombie cant be killed, exit loop
                failed = True
                break
            l, r, k = u[-1]
            dmg = min(k,zmbs[zi])
            zmbs[zi] -= dmg
            ans += dmg
            d[l-1] -= dmg
            d[r] += dmg
            u[-1][-1] -= dmg
            if u[-1][-1] == 0: u.pop()
        if failed: break
    if failed: print('NO')
    else: print('YES', ans)
