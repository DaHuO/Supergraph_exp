import math

def generateJamcode (length, counter):
    jam = [];
    jam.append(1);
    for i in range(length-2, 0, -1):
        #print i-1;
        if (counter / (2 ** (i-1))) != 0:
            jam.append(1);
        else:
            jam.append(0);
        counter = counter % (2 ** (i-1));
                
    jam.append(1);
    return jam;

def numberInBase10 (jamcode, base):
    retVal = "";
    
    for i in range(0,len(jamcode)):
        retVal += str(jamcode[i]);

    #print retVal;
    
    return int(retVal,base);

def devideJamCode (jamcode):
    devisors = [];
    for base in range(2,11):
        num = numberInBase10(jamcode, base);

        smallestDiv = smallestDevisor(num);
        devisors.append(smallestDiv);
        #print num;
        
    for divs in devisors:
        if divs < 0:
            return False;

    return devisors;

def smallestDevisor (number):
    div = 2;
    while div < math.sqrt(number):
        if number % div == 0:
            return div;
        div += 1;

        if div > 100000:
            return -1;
    return -1;
    

f = open('C-large.in', 'r');
f2 = open('resultLarge.txt', 'w');

T = f.readline();

for case in range(0, int(T)):
    line = f.readline();
    line = line.rstrip('\n');
    numbers = line.split(' ');
    N = int(numbers[0]);
    J = int(numbers[1]);
    #print N;
    #print J;
    successJam = 0;
    counter = 0;
    f2.write("Case #" + str(case+1) + ":\n");
    while successJam < J:
        possibleJam = generateJamcode(N, counter);
        temp = devideJamCode(possibleJam);
        if temp != False:
            for el in possibleJam:
                f2.write(str(el));
            for el in temp:
                f2.write(" " + str(el));
             
            successJam += 1;
            f2.write("\n");
        
        counter += 1;
    
f.close();
f2.close();
