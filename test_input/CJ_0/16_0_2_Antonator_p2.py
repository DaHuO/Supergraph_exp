f = open('B-large.in', 'r');
f2 = open('resultLarge.txt', 'w');

T = f.readline();

done = False;

for case in range(0, int(T)):
    line = f.readline();
    line = line.rstrip('\n');
    arrayPan = []
    for letter in line:
        if letter == '+':
            arrayPan.append(1);
        if letter == '-':
            arrayPan.append(0);
   # print arrayPan;

    ops = 0;

    while True:

        #print arrayPan;
        
        done = True;
        for el in arrayPan:
            #print el;
            if el == 0:
                done = False;
                break;

        if done:
            f2.write("Case #" + str(case+1) + ": " + str(ops) + '\n');
            break;

        # get index of alternating
        index = len(arrayPan);
        for i in range(1, len(arrayPan)):
            if arrayPan[i-1] != arrayPan[i]:
                index = i;
                break;
            
        #print "index: " + str(index);


        # do swap before index
        flipList = arrayPan[0:index];
        remainList = arrayPan[index:];

        #invert flip list
        for i in range(0, len(flipList)):
            if flipList[i] == 0:
                flipList[i] = 1;
            else:
                flipList[i] = 0;

        flipList.reverse();


        #print flipList;
        #print remainList;

        arrayPan = flipList + remainList;

            

        ops += 1;


f.close();
f2.close();
