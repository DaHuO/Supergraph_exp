# -*- coding: utf-8 -*-
######################################################
##                                                  ##
##  Fran Muñoz                                      ##
##  email: fran.mzy@gmail.com                       ##
##  UVA user: franmzy                               ##
##  Linkedin: https://www.linkedin.com/in/franmzy   ##
##                                                  ##
######################################################

n_cases = int(input())

for i_case in range(n_cases):

  s = input()

  result = s[0]

  for x in s[1:]:
    if x >= result[0]:
      result = x + result
    else:
      result = result + x

  print('Case #{0}: {1}'.format(i_case+1, result))



