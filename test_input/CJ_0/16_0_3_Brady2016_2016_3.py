import math

def base(str,base):
    arr=list(str)
    leng=len(arr)
    result=0
    for index in range(leng):
        if arr[index]=='1':
            result=result+int(arr[index])*math.pow( base, leng-index-1)
    return int(result)

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):    
        if n % i == 0:
            return i
    return 0 

def jamcoin(string):
    result=string[:];
    for basenum in range (2,11):
        primerseult=prime(base(string,basenum))
        if primerseult!=0:
            result=result+" "+ str(primerseult)
        else:
            break
    else:
        return result
    return 0

def getalljamcoin(n,j):
    binnum=0
    howmany=0
    result=["Case #1:\n"]
    while(1):
        string="1"
        string=string+str(bin(binnum)[2:].zfill(n-2))    
        string=string+"1"
        output=jamcoin(string)
        if output!=0:
            howmany=howmany+1
            result.append(output+"\n")
        if howmany>=j:
            return result
        binnum=binnum+1



file_object = open('2016_3_1.txt', 'w+')
file_object.writelines(getalljamcoin(16,50))
file_object.close( )
'''
file_object = open('2016_3_2.txt', 'w+')
file_object.writelines(getalljamcoin(32,500))
file_object.close( )
'''
print('DONE')