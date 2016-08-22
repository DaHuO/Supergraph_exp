input=open("A-large.in","r")
output=open("PAlarge.txt","w")

T = int(input.readline())

for loop in range(T):
    w = input.readline()
    lw = w[0]
    for i in range(1,len(w)):
        if w[i] >= lw[0]:
            lw = w[i]+lw
        else:
            lw = lw+w[i]
    output.write("Case #{}: {}".format(loop+1,lw))

input.close()
output.close()