def remove_endlines(orignal_data):
    new_data=""
    orignal_data=orignal_data.replace('\r','')
    orignal_data=orignal_data.replace('\n','')
    if orignal_data!="":
        new_data=orignal_data
    return new_data

def flip_sign(orignal_data):
    if orignal_data=="+":
        return "-"
    else:
        return "+"

def flip_data(orignal_data):
    DatatoFlip=orignal_data[::-1]
    new_data=""
    for j in DatatoFlip:
        new_data+=flip_sign(j)
    return new_data


testfile=open('B-large.in','r')
ndata=testfile.readlines()
for k in range(1,len(ndata)):
    Data=remove_endlines(ndata[k])[::-1]
    FinalData=""
    TempData=""
    for i in range(len(Data)):
        FinalData+='+'
    Num=0
    while TempData != FinalData:
        if Data[0]=='+':
            Data=Data[1:]
            TempData+='+'
        else:
            Data=flip_data(Data)[::-1]
            Num+=1
    print "Case #{}:".format(k),Num
testfile.close() 
