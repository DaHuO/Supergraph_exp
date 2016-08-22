from bitarray import bitarray
import collections

def pancakes(case,init_pc,length):
    if(init_pc.all()):
        print("Case #{0}: 0".format(case))
        return
    
    q = collections.deque()
    visit = set()
    current = (init_pc,0)

    q.append(current)
    while True:
        current = q.popleft()

        current_str = current[0].to01()
        if current_str in visit:
            continue
        
        visit.add(current_str)
        for i in range(1,length+1):
            flip = current[0][:i]
            flip.reverse()
            flip.invert()
            flipped = flip + current[0][i:]

            if flipped.all():
                print("Case #{0}: {1}".format(case,current[1]+1))
                return
            state = tuple([flipped,current[1]+1])
            q.append(state)
    return

cases = int(input())
for i in range(1,cases+1):
    inp = input()
    
    pc2b = {'+':bitarray('1'),'-':bitarray('0')}
    init_pc = bitarray()
    init_pc.encode(pc2b,inp)
    pancakes(i,init_pc,len(inp))
