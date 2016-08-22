# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 18:39:13 2016

@author: caiyi
"""

"""
new 
"""
end = "11"
start = "11"
res = set()
import numpy as np
while len(res) < 500:
    ind = np.random.randint(2, size = 14)
    mid = ''
    for i in ind:
        if i == 0:
            mid += '00'
        else:
            mid += '11'
    res.add(start + mid + end)
div = [str(i) for i in range(3,12)]

file_name = 'res_C_large.txt'
with open(file_name,'w') as f:
        res_str = 'Case #1:\n'
        for tmp in res:
            res_str += tmp + ' ' + ' '.join(div) + '\n'
        f.write(res_str)
