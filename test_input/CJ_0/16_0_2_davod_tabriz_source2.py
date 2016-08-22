# codejam2016 qualification round source 2
#
from decimal import Decimal
def  assign(a,b,k):
 list1 = list(a)
 list1[k]=b;
 return ''.join(list1)
def swap(a,m,k):
 list1 = list(a)
 list1[m],list1[k]=list1[k],list1[m]
 return ''.join(list1)
with open('D:\dawood\codejam\codejam\codejam\codejam\codejam2016\qualification\input2.in', 'r+') as fin:
 with open('D:\dawood\codejam\codejam\codejam\codejam\codejam2016\qualification\output2.out', 'r+') as fout:
    a = [int(x) for x in fin.readline().split()] # read first line

    for i in range(a[0]):
     b =fin.readline();
     flipCount = 0;
     for j in range(len(b) - 1,-1,-1) :
                    if (b[j] == '+'):
                        continue;
                      
                    else :
                        flipCount+=1
                        if (b[0] == '+') :
                            flipCount+=1
                            l = 0;
                            while (b[l] == '+') :l+=1;

                            for  k in range( 0, l / 2) :
                                
                                swap(b,k,1-k-l)

                            for k in range(0,l): 
                                if b[k]=='+':
                                   b= assign(b,'-',k)
                                else:
                                   b= assign(b,'+',k) 
                             
                             
                        
                        l = j + 1;
                        for k in range(0,l/2):
                            
                            swap(b,k,l-k-1)
                       

                        for k in range(0,j+1): 
                            if b[k]=='+':
                                   b= assign(b,'-',k)
                            else:
                                   b= assign(b,'+',k) 
                         
                     
     print flipCount