t = int(input().strip())

for _ in range(t):
    n, m = (int(__) for __ in input().strip().split())
    completed = [int(c) for c in input().strip().split()]
    completed.sort()
    #completed.append(0)
    chef = []
    assistant = []
    chef_flag = True
    c_index = 0
    c_len = len(completed)
    for job in range(1, n+1):
        if(c_index != c_len and completed[c_index] == job):
            c_index += 1
            continue
        #below works :D
        #if job in completed: continue
        chef.append(str(job)) if chef_flag else assistant.append(str(job))
        chef_flag = not chef_flag
    print(' '.join(chef)) if chef else print() 
    print(' '.join(assistant)) if assistant else print()