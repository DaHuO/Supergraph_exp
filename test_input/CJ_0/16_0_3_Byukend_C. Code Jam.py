# -*- coding: utf-8 -*-
# @Author: Byukend
# @Date:   2016-04-09 16:33:33
# @Last Modified by:   Byukend
# @Last Modified time: 2016-04-09 16:33:33




def getDec(binary, base):
    result = 0
    # print(binary)
    for i in range(len(binary) - 1, -1, -1):
        result += (base * int(binary[i]))**(len(binary) - 1 - i)
    return result

def checkPrime(x):
    if x% 2==0:
        return 2
    i = 3
    while i < x**0.5:
        if x%i ==0:
            return i
        i+= 2
    return 0

def main():
    t = int(input())
    for i in range(1, t + 1):
        n, j = map(int, str.split((input())))
        print('Case #{0}:'.format(i))
        max_center = 2**(n - 2) - 1
        form = '{0:0b}'
        if n - 2 > 0:
            form = str(n - 2).join([form[0:4], form[4:]])
        # print(form.format(max_center))
        runner = 0
        k = 1
        while k <= j:
            curr_jam = ''.join(['1', form.format(runner), '1'])
            runner += 1
            if runner > max_center:
                return
            ans = curr_jam
            for x in range(9):
                dec = getDec(curr_jam, x + 2)
                trav = checkPrime(dec)
                # print(getDec(curr_jam, x + 2), trav)
                if trav != 0:
                    ans = ' '.join([ans, str(trav)])
                else:
                    ans = ''
                    break
            if len(ans) > 0:
                print(ans)
                ans = ''
                k += 1


if __name__ == '__main__':
    main()
