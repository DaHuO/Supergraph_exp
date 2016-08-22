inp= open('in1.txt', 'r')
inp_list = [x for x in inp.read().split('\n')]

n = int(inp_list.pop(0))
num = set()
answer = []
f = open("output1.txt", "w")

def to_num(a):
    a = str(a)
    result = set()
    for i in a:
        result.add(i)
    return set(result)

for i in range(n):
    cur = set()
    S = list(inp_list[i])
    answer = ""
    answer += S.pop(0)
    for x in S:
        if(ord(x) >= ord(answer[0])):
            answer = x + answer
        else:
            answer = answer + x
    f.write("Case #" + str(i+1) + ": " + answer + "\n")
inp.close()
f.close()
