#!/usr/local/bin/python


f = open ("B-large.in", "rb")
T=int(f.readline())

flippy = 0

def main():
    for i in range(T):
        s = f.readline()

        mixy(tolist(s))
        print "Case #"+str(i+1)+": "+str(flippy)
        reset()

def tolist(s):
    result = []
    for l in s:
        result.append(l)
    return result

def reset():
    global flippy
    flippy = 0



def mixy(lst):
    global flippy
    pluslst = []
    minuslst = []
    if not "-" in lst:
        return
    if not "+" in lst:
        flippy+=1
        return
    for idx in range(len(lst)):
        if lst[idx]=="+":
            pluslst.append(idx)
        else :
            minuslst.append(idx)
    if lst[0] == "+":
        flippy+=1
        newlst=lst[minuslst[0]:]
        mixy(newlst)
        return
    newlst =lst[pluslst[0]:]
    flippy+=1
    mixy(newlst)
    return
                        
    

    




if __name__ == "__main__":
    main()
