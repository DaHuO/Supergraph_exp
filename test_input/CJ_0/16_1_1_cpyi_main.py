# Read it
fin_s = "A-large.in"
fou_s = fin_s + '.out'
fin = open(fin_s, 'r')
fou = open(fou_s, 'w')

# Solve it
T = int(fin.readline())

for t in range(T):
    white_board = ""
    
    # Read routines
    word = fin.readline().strip()
    for i in range(len(word)):
        if len(white_board) == 0:
            white_board = white_board + word[i]
        else:
            if word[i] + white_board > white_board + word[i]:
                white_board = word[i] + white_board
            else:
                white_board = white_board + word[i]
    
    # Write routines
    fou.write('Case #' + str(t + 1) + ': ' + white_board + '\n')
    
# Finish it
fin.close()
fou.close()