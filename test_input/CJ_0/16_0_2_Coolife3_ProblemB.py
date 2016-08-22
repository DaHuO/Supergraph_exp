
# coding: utf-8

# In[11]:

def problem_B(infileName, outputName):
    infile = open(infileName, 'r')
    outfile = open(outputName, 'w')
    
    lines = infile.readlines()
    
    for i in range(1, len(lines)):
        pancake = lines[i].rstrip('\n')
        output = "Case #" + str(i)
        
        ans = flip_pancake(pancake)
        
        output += ": " + str(ans) + "\n"
        outfile.write(output)        


def flip_pancake(pancake):
    if pancake == '+':
        return 0
    if pancake == '-':
        return 1
    i = len(pancake) - 1
    while i >= 0 and pancake[i] == '+':
        i = i - 1
    if i == -1:
        return 0
    j = 0
    new_pancake = ""
    while j <= i:
        if pancake[j] == '+':
            new_pancake += '-'
        else:
            new_pancake += '+'
        j += 1    
    return 1 + flip_pancake(new_pancake)
        
        
problem_B("B-small-attempt0.in", "B_small_out")
        


# In[ ]:



