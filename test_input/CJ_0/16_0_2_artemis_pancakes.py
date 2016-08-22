t = int(raw_input())
x=1
mylist = [];

def make_list(test) :
    count = 0
    a=0
    for p in test :
        work.append(p)
        if a!=p :
           count+=1
        a=p
    if p == '+' :
       count-=1
    return count

while t>0 :
      work = [];
      test = str(raw_input())
      a = make_list(test)
      mylist.append('Case #'+str(x)+': '+str(a))
      x+=1
      t-=1

for p in mylist :
    print p
