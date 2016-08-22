import sys

def lastWord(s):
    l=list(s)
    res=[]
    for c in l:
        if res == []:
            res.append(c)
            continue
        if c>=res[0]:
            res.insert(0,c)
        else:
            res.append(c)
    return ''.join(res)






def main():
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
    for i in range(1,len(lines)):
        res = lastWord(lines[i])
        print('Case #%d: %s' % (i,res))



if __name__ == '__main__':
    main()