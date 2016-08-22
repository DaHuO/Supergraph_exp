def flip(s):
    d={'+':'-','-':'+'}
    return [d[i] for i in s]

def fun(s):
    l=len(s)
    if l==1:
        if s[0]=='+': return 0
        else: return 1
    if s[-1]=='-':
        if s[0]=='+':
            for i in s:
                if i=='+': i='-'
                else: break
            return 1+fun(s[::-1])
        else:
            return 1+fun(flip(s)[::-1])
    else:
        return fun(s[:-1])


n=int(input())
for i in range(n):
  s=input()
  ans=fun(s)
  print('Case #{0}: {1}'.format(i+1,ans))
