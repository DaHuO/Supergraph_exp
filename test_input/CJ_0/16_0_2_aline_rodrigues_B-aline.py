import sys

def invert_vector(vector,end):
    inverted = []
    for i in xrange(0,end):
        inverted.append('+' if vector[i]=='-' else '-')
    for i in xrange(0,end):
        vector[i]=inverted[end-i-1]

read_file = open(sys.argv[1],"r")
items = read_file.readlines()

for i in xrange(0,len(items)):
    items[i] = items[i].split('\n')[0]

write_file = open(sys.argv[2],"w")
for j in xrange(1,int(items[0])+1):
    current_vector = list(items[j])
    changes = 0
    position = len(current_vector)-1
    while (position>-1):
        if current_vector[position]=='-':
            if current_vector[0]=='-':
                invert_vector(current_vector,position+1)
                changes = changes + 1
            else:
                search = 0
                while current_vector[search]=='+':
                    search = search + 1
                invert_vector(current_vector,search)
                changes= changes + 1
        else:
            position= position - 1
        
    write_file.write('Case #'+str(j)+': '+str(changes)+'\n')

write_file.close()


