
def codeJam(case,n):
        print ("case #{0}:".format(case),end=' ')
        li=""
        for i in range(len(n)):
                if(i==0):
                        li=n[i]
                else:
                        if(n[i]>=li[0]):
                                li=n[i]+li
                        else:
                                li=li+n[i]
        print(li)
def main():
        T=int(input())
        for i in range(T):
                n=str(input())
                n=list(n)
                codeJam(i+1,n)
main()
