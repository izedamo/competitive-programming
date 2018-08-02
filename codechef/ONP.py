def rpn(ex):
    stk = []
    out = ''
    for char in ex:
        if char.isalpha(): out += char
        elif char in ['^', '/', '*', '+', '-']:
            while(len(stk) != 0 and stk[0] != '(' and prty[stk[0]] >= prty[char]):
                out += stk.pop(0)
            stk.insert(0, char)
        elif char == '(': stk.insert(0, char)
        elif char == ')':
            while(stk[0] != '('):
                out += stk.pop(0)
            stk.pop(0)
    while(len(stk) != 0):
        out += stk.pop(0)
    return out

prty = {'^': 3, '/': 2, '*': 2, '+': 1, '-': 1}
#print(prty['/'])
t = int(input().strip())
exs = []
for i in range(t):
    ex = input().strip()
    print(ex[1:-1])
    print(rpn(ex[1:-1]))
