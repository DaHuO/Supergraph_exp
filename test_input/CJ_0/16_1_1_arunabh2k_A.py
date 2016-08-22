#!/usr/bin/python

f = open('sample.txt', 'r')
tc = int(f.readline())
#print tc
for index in range(tc):
    line = f.readline().rstrip()
    arr = []
    arr += line
    slen = len(arr)
    code = ""
    for i in range(slen):
        if code == "":
            code = str(arr[i])
            continue
        if code[0] >  arr[i]:
            code += str(arr[i])
        else:
            code = str(arr[i]) + code

    print "CASE #" + str(index+1) + ": " +  code
