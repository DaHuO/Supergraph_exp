# -*- coding: utf-8 -*-
# @Author: Byukend
# @Date:   2016-04-09 09:26:37
# @Last Modified by:   Byukend
# @Last Modified time: 2016-04-09 09:26:37


def flip(flipee):
    flipee = flipee[::-1]
    flipee = flipee.replace('+', 't')
    flipee = flipee.replace('-', '+')
    flipee = flipee.replace('t', '-')
    return flipee


def first_minus_from_back(stk):
    count = 0
    for i in stk[::-1]:
        count += 1
        if i == '-':
            # print(stk[len(stk)-count], len(stk)-count)
            return len(stk) - count


def flip_top(stk):
    for i in range(len(stk)):
        if(stk[i] == '+'):
            stk = stk.replace('+','-',1)
        else:
            return stk


def main():
    n = int(input())
    for rnd in range(n):
        stk = input()
        count = 0
        while(stk.count('+') != len(stk)):        
            
            if stk[0] == '+':
                stk = flip_top(stk)
                count += 1
            if stk.count('+') == len(stk):
                break
            last_blank = first_minus_from_back(stk)
            
            stk = flip(stk[0:last_blank + 1]) + stk[last_blank+1:]
            # print(stk)
            count += 1
            if stk.count('+') == len(stk):
                break
        print("Case #",rnd+1,': ',count,sep ='')


if __name__ == '__main__':
    main()
