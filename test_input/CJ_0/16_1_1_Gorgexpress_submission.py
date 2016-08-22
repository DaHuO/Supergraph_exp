def last_word(word):
    best = [word[0]]
    for i in xrange(1, len(word)):
        if word[i] < best[0]:
            best.append(word[i])
        else:
            best.insert(0, word[i])
    return best
        


out = open("A.out", "w")
with open("A.in") as f:
    f.next()
    T = 1
    for line in f:
        word = line[:len(line) - 1]
        best = last_word(word)
        out.write("Case #{}: {}\n".format(T, "".join(best)))
        T += 1
        
        
        
        
            
out.close()