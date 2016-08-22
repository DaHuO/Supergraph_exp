
##The libraries below are standard python
##The distribution of python I am using is pyzo, with intro message:
#####Python 3.4.1 |Continuum Analytics, Inc.| (default, May 19 2014, 13:02:30) on Windows (64 bits).

#Code was run using this interpreter, but final outputs were 
#generated using the command-line version of the same distribution:
#####This is the IEP interpreter with integrated event loop for PYSIDE.
#####Using IPython 2.1.0 -- An enhanced Interactive Python.
import numpy as np
import pylab as pl
import re 
import scipy as sc
import sys 
f = "foo" 


##Only have one choice per round...increase value or not



##fstem    = "415A/A-small-attempt0"
fstem    = "415A/A-large"
fname_in = ('c:/Users/Fini/Documents/Career/Google/Code Jam/' + 
            fstem + '.in')
#fname_out = ('c:/Users/Fini/Documents/Career/Google/Code Jam/' + 
#            fstem + '.out')

####SWAP TWO LINES TO SWITCH FROM STDIN TO FILE INPUT
in_trimmed = lambda f: f.readline()[:-1]
#in_trimmed = lambda f: input()
#if(True):
with open(fname_in, 'r') as f:
    Ncases = int(in_trimmed(f))
    CaseIn = [ [] for ncase in range(Ncases)]
    for ncase in range(Ncases):
        SS = in_trimmed(f)
        CaseIn[ncase] = SS




for ncase in range(Ncases):
  SS = CaseIn[ncase] 
  result = "" + SS[0]
  for jj in range(1,len(SS)):
      if(ord(SS[jj]) >= ord(result[0])):
          result = SS[jj] + result
      else:
          result = result + SS[jj] 
  print("Case #{}: {}".format(ncase+1, result))


##We can double-check ...actually 100 is reasonably tight with 125 being one of the outliers
#nvec = [NN for NN in range(10**5)]
#mulvec = [-1 for NN in nvec]
#for NN in nvec:
#  if(NN==0):
#      mulvec[NN] = 0
#  else:
#      remainder = set('0123456789')
#      mult = 0
#    ##Once you get past ??... multiplying won't help
#      while((mult <= 100) and (len(remainder)>0)):
#          mult += 1
#          remainder = remainder.difference(set("{}".format(mult * NN)))
#          if(len(remainder) != 0):
#              result = "ERROR"
#              mulvec[NN] = -2
#          else:
#              result = "{}".format(mult * NN)
#              mulvec[NN] = mult
#  
#pl.plot( np.array(nvec), np.array(mulvec))
