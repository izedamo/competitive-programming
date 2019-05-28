t = input().strip()

for i in range(int(t)):
    n = int(input().strip())
    d = [None] * (n-1)
    s = [int(i) for i in input().strip().split()]
    s.sort()
    for j in range(n-1):
        d[j] = s[j+1] - s[j] #calculating difference array.
    print(min(d))