file = open("B-large.in","r")
contents = file.readlines()
numbers = contents[0].strip()
ns= [contents[i].strip() for i in range(1,int(numbers)+1)]
results=[]


def flipping(n):
    result=0
    sign=n[0]
    for k in range(len(n)):
        if n[k]!=sign:
            result+=1
            sign=n[k]
    if n[-1]=="-":
        result += 1
    return result

for n in ns:
    results.append(flipping(n))


file.close()
file=open("test_out.txt","w")
for i in range(int(numbers)):
    file.write("Case #{0}: {1}\n".format(i+1,results[i]))
file.close()
