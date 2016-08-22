__author__ = 'Hp Pc'

inputFile = open("input.txt", 'r');
outputFile = open("output.txt", 'w');
count = int(inputFile.readline());
lineno = 1;

while lineno <= count:
    inp = inputFile.readline().split();
    length = int(inp[0]);
    samples = int(inp[1]);
    num = [0] * (length - 2);
    found = 0;
    line = "Case #" + `lineno` + ": " + "\n";
    outputFile.write(line);
    while found < samples:
        divisorList = "";
        for base in range(2, 11):
            basenum = 1 + pow(base, length - 1);
            for iter in range(0, length - 2):
                basenum = basenum + num[iter] * pow(base, iter + 1);
            divisor = 2;
            while basenum % divisor != 0 and divisor < 1024:
                divisor = divisor + 1;
            if basenum % divisor != 0:
                break;
            else:
                divisorList =divisorList +`divisor`+" ";
        if basenum%divisor==0 and base==10:
            found = found + 1;
            line = str(basenum)+" " + divisorList.rstrip() + "\n";
            outputFile.write(line);

        for iter in range(0, length - 2):
            if num[iter] == 0:
                num[iter] = 1;
                break;
            else:
                num[iter] = 0;


    lineno = lineno + 1;
inputFile.close();
outputFile.close();
