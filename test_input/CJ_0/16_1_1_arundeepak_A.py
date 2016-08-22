'__author__'=='deepak Singh Mehta(learning to code :) ) '
 
'''
    Hard work beats Talent when Talent doesn't work hard. :)
'''


if __name__=='__main__':
    tests = int(input())
    for case in range(1,tests+1):
        string = input()
        st = ''
        for i in string:
            if len(st)==0:
                st += i
            else:
                if st[0] > i:
                    st += i
                else:
                    st =i + st
        print("Case #"+str(case)+":",st)
