import sys
from collections import deque


def check_flips(S):

    queue = deque()
    #Transform sequence to 1 and 0
    for s in S:
        if s == '+':
            queue.append(1)
        else:
            queue.append(0)

    num_flips = 0
    while queue: #not empty

        #First, remove 1's from right end (bottom of the pile
        while queue:
            s = queue.pop()
            if s == 0:
                queue.append(s)
                break
        #if queue is already empty, return num_movements
        if not queue:
            return num_flips

        #Flip remaining
        queue_tmp = deque()
        num_flips+=1
        while queue: #Revert remaining in queue
            s = queue.popleft()
            queue_tmp.append(1-s)
        queue = queue_tmp
    return num_flips


def test_generate_input(max_length,num_cases):
    import random
    cases = []
    for i in range(num_cases):
        num_char = random.randint(1,max_length)
        case = ''.join(random.choice('+-') for i in range(num_char))
        cases.append(case)
    return cases


if __name__ == "__main__":

    T = int(sys.stdin.readline()) #number of test cases

    for i in xrange(1,T+1):
         S = sys.stdin.readline().strip()
         print 'Case #%d: %s' %(i,check_flips(S))


    #cases = test_generate_input(max_length=100,num_cases=100)

