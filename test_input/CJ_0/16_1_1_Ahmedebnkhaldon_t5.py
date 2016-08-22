testfile=open('A-large.in','r')
ndata=testfile.readlines()
for k in range(1,len(ndata)):
    ndata[k]=ndata[k][:len(ndata[k])-1]
    Out=ndata[k][0]
    for i in ndata[k][1:]:
        if i<Out[0]:
            Out=Out+i
        else:
            Out=i+Out
    print "Case #{}:".format(k),Out
testfile.close() 
