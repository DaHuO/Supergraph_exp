import Queue

def flip(cakes, i):
    s_cakes = ''
    temp_cakes = cakes[:i]
    for cake in temp_cakes:
        if (cake == '+'):
            s_cakes += '-'
        else:
            s_cakes += '+'

    return s_cakes[::-1] + cakes[i:]

def bfs(cakes):

    q = Queue.Queue()
    q.put(cakes)

    list_states = []
    current_state = ''
    final_state = ''
    trace = {}

    while not q.empty():
        current_state = q.get()
        if '-' not in current_state:
            final_state = current_state
            break
        list_states.append(current_state)
        for i in range(1,len(current_state)+1):
            new_state = flip(current_state, i)

            if new_state not in list_states:
                trace[new_state] = current_state
                list_states.append(new_state)
                q.put(new_state)

    result = 0
    state = final_state
    while (state != cakes):
        result += 1
        state = trace[state]
    return result

f_read = open('B-small-attempt0.in','r')
f_write = open('B-small-attempt0.out','w')
t = int(f_read.readline())
for k in range(t):
    cakes = f_read.readline()
    print k, ' ' , cakes
    f_write.write('Case #{0}: {1}\n'.format(str(k+1),str(bfs(cakes))))
f_read.close()
f_write.close()
