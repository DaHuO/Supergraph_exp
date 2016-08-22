import pdb
import sys
import getopt
from collections import defaultdict
from sets import Set

def flip(cakes):
    flip_dict = {"+":"-","-":"+"}
    c_vec = [flip_dict[i] for i in cakes]
    return "".join(c_vec)

def flip_pancakes2(cakes):
    l1 = len(cakes)
    count = 0
    while l1 > 0:
        if cakes[-1] == "-":
            cakes = flip(cakes)
            count = count + 1
            cakes = cakes[:-1]
            l1 = len(cakes)
        else:
            cakes = cakes[:-1]
            l1 = len(cakes)
    return count



def flip_pancakes1(cakes):
    #import pdb;pdb.set_trace()
    all_up = (sum([i == "+" for i in cakes]) == len(cakes)) * 1
    all_down = (sum([i == "-" for i in cakes]) == len(cakes)) * 1
    if all_up == 1:
        return 0
    if all_down == 1:
        return 1
    if cakes == "+-":
        return 2
    if cakes == "-+":
        return 1
    if len(cakes) == 1:
        if cakes == "-":
            return 1
        if cakes == "+":
            return 0
    elif len(cakes) > 2:
        top_ind = len(cakes)/2
        return flip_pancakes1(cakes[:top_ind]) + flip_pancakes1(cakes[top_ind:])


def flip_pancakes(cakes):
    #import pdb;pdb.set_trace()
    all_up = (sum([i == "+" for i in cakes]) == len(cakes)) * 1
    all_down = (sum([i == "-" for i in cakes]) == len(cakes)) * 1
    if all_up == 1:
        return 0
    if all_down == 1:
        return 1
    if cakes == "+-":
        return 2
    if cakes == "-+":
        return 1
    if len(cakes) == 1:
        if cakes == "-":
            return 1
        if cakes == "+":
            return 0
    elif len(cakes) > 2:
        if cakes[0] == "+":
            down_flag= 1*(sum([i == "-" for i in cakes[1:]]) == (len(cakes)-1))
            if down_flag == 1:
                return 2
        if cakes[-1] == "-":
            down_flag= 1*(sum([i == "+" for i in cakes[1:]]) == (len(cakes)-1))
            if down_flag == 1:
                return 1
        top_ind = len(cakes)/2
        return flip_pancakes(cakes[:top_ind]) + flip_pancakes(cakes[top_ind:])


def getRes(temp):
    outname = "/Users/Work/Desktop/output.txt"
    fh1 = open(outname, 'w')
    for i in range(len(temp)):
        cakes = temp[i]
        count = i + 1
        res = flip_pancakes(cakes)
        res1 = flip_pancakes1(cakes)
        res2 = flip_pancakes2(cakes)
        print min([res, res1, res2]), cakes
        tstr = "Case #"+str(count)+": "+str(res2)
        print >>fh1, tstr
    fh1.close()
    



def main():
    fname = sys.argv[1]
    fh = open(fname, 'r')
    count = 0
    temp = []
    tot_num = 0
    for l in fh:
        if(count == 0):
            tot_num = int(l.strip())
        if(count > 0):
            temp.append(l.strip())
        count += 1
    getRes(temp)
    fh.close()

if __name__ == '__main__':
    main()