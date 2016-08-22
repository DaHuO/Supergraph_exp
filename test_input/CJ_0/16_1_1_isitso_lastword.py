from sys import argv

def addChar(word, char):
    """ Add a character to the right of the word if it is 'smaller' than 
    first character of the word. to the left otherwise
    """
    return word + char if len(word) > 0 and word[0] > char else char + word
    
def main():
    script, filename = argv
    in_file = open(filename, 'r')
    out_file = open(filename.split('.')[0] + '.out', 'w')
    list = []
    num = 0
    try:
        for i, line in enumerate(in_file):
            print(line)
            if not i: num = int(line.strip())
            else : list.append(line.strip().upper())
    except:
        pass
    in_file.close()
    
    for i, w in enumerate(list):
        word = ''
        for c in w:
            word = addChar(word, c)
        out_file.write('Case #' + str(i+1) + ': ' + word + '\n')
    out_file.close()

if __name__ == '__main__':
    main()