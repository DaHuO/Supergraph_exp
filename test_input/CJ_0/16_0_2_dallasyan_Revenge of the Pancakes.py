with open("inp.txt") as f:
    with open("out.txt","w+") as g:
        i=0
        for line in f:
            line=line.strip()
            if i==0:
                lines=int(line)
            else:
                k=0
                a=1
                for m in range(len(line)):
                    if line[m]=="-":
                        a=0
                while a==0:
                    a=1
                    b=-1
                    if line[0]=="+":
                        for m in range(len(line)):
                            if line[m]=="-":
                                break
                        line="-"*(m+1)+line[m+1:]
                        k+=1
                    else:
                        for m in range(len(line)):
                            if line[m]=="+":
                                break
                            line="+"*(m+1)+line[m+1:]
                        k+=1
                    for m in range(len(line)):
                        if line[m]=="-":
                            a=0
                print("Case #"+str(i)+": "+str(k))
                g.write("Case #"+str(i)+": "+str(k)+"\n")
            i+=1
