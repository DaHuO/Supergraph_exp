# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 21:27:32 2016

@author: jon
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 00:30:30 2016

@author: jon
"""
# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io


def solveA(Li):
    Mi=list(Li[0])
    b=max(Mi)
    startcount=0
    for i in Mi:
        if i==b:
            startcount=startcount+1
    start=[b]*startcount
    middle=[]
    end=[]
    stop=0
    for i in Mi:
        if i==b:
            stop=1
        if i!=b:
            if stop==0:
                middle=middle+[i]
            if stop==1:
                end=end+[i]
    for k in range (0,5):
        if len(middle)>0:
            middle="".join(middle)
            middle=solveA([middle])
            middle=list(middle)
  #  print(start)
  # print(middle)
  #  print(end)
  #  print("**************")
    lastword=start+middle+end
    lastword=''.join(lastword)
    return(lastword)

    
def solve(infname, outfname):
    L= codejam_io.read_simple(infname, str)
    results = [solveA(Li) for Li in L]
    codejam_io.write_simple(outfname,results)
   
    
#solve("A-sample.in", "A-sample.out")   
#solve("A-small-attempt0.in", "A-small-attempt0.out")    
#solve("A-small-attempt1.in", "A-small-attempt1.out")   
#solve("A-small-attempt2.in", "A-small-attempt2.out")     
solve("A-large.in", "A-large.out")     