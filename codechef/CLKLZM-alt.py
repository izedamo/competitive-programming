# finish zombies one by one, use greedy approach and difference array.

#import heapq <- use doing priority queue
#TODO: difference array.

from sys import stdin

t = int(stdin.readline())
for i in range(t):
    (n, m) = (int(x) for x in stdin.readline().split())
    zmbs = [int(x) for x in stdin.readline().split()]
    diff = [z[i]-z[i-1] for i in range(1:len(zmbs))] # difference array
    lrk = []
    for j in range(m):
        l, r, k = map(int, stdin.readline().split())
        lrk.append([l, r, k])
    u = []
    ans = 0
    failed = False
    zkilled = 0
    for zi in range(len(zmbs)):
        u += [x for x in lrk if x[0] == zi+1]
        u.sort(key=lambda x: x[1])
        z = zmbs[zi]
        if z <= 0: zkilled += 1
        else:
            while(z > 0):
                if u == [] or u[-1][1] < zi+1:
                    failed = True
                    # z cant be killed, exit loop
                    break
                l, r, k = u[-1]
                if k > z:
                    ans += z
                    u[-1][-1] -= z
                    zmbs[zi:r] = [x-z for x in zmbs[zi:r]]
                    z = 0
                    zkilled += 1
                else:
                    ans += k
                    z -= k
                    if z == 0: zkilled += 1
                    zmbs[zi:r] = [x-k for x in zmbs[zi:r]]
                    u.pop()
        if failed: break
    if zkilled != len(zmbs): print('NO')
    else: print('YES', ans)
