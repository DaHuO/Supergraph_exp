"""
Do[good = 1; answer = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; 
 Do[test = FromDigits[IntegerString[i, 2], b]; 
  If[PrimeQ[test], good = 0, 
   answer[[b]] = First[First[FactorInteger[test]]]], {b, 2, 10}];  
 If[good == 1, Print[i]; Print [answer]], {i, 2^15 + 1, 2^15 + 500, 
  2}]
"""

"""
Do[good = 1; answer = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; 
 Do[test = FromDigits[IntegerString[i, 2], b]; 
  If[PrimeQ[test], good = 0, 
   answer[[b]] = First[First[FactorInteger[test]]]], {b, 2, 10}];  
 If[good == 1, Print[i]; Print [answer]]; 
 q += 1, {i, 2^31 + 1, 2^31 + 2000, 2}]
"""

print 'Case #1:'
f = file('c2.txt', 'r').readlines()
for i in range(500):
    a = f[i * 2]
    b = f[i * 2 + 1]
    a = int(a[a.index('=') + 2:])
    b = b.strip()[b.index('=') + 3:-1].split(',')[1:]
    print bin(a)[2:] + ' ' + ' '.join(b)
