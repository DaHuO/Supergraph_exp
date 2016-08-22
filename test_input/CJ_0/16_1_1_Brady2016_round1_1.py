def mysort(word):
    result=" "
    for letter in word:     
        if(result[0]>letter):
            result=(result+letter)
        else:
            result=(letter+result).strip()
    return result
        
        
file = open("a")
T = file.readline()
all_the_text=[]

for num in range(1,int(T)+1):
    word=file.readline().strip()
    final=mysort(word)
    temstr='Case #'+str(num)+': '+final+'\n'
    all_the_text.append(temstr)
    
file_object = open('thefile.txt', 'w+')
file_object.writelines(all_the_text)
file_object.close( )