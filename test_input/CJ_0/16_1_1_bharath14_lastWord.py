__author__ = 'bharath'
def main():
    t=input()
    for i in range(1,t+1):
        print "Case #%d:"%(i),
        s=raw_input()
        res=""
        for i in s:
            if res=="":
                res+=i
            elif res[0]>i:
                res+=i
            else:
                res = i+ res
        print res

if __name__ == "__main__":
    main()