def n_flips(inFile, outFile):
    def write_output(g, n_case, output):
        #print("Case #" + str(n_case) + ": " + str(output))
        g.write("Case #" + str(n_case) + ": " + str(output) + '\n')

    f = open(inFile, 'r')
    g = open(outFile, 'w')
    n_lines = int(f.readline())
    if n_lines == 0:
        return

    for n_case in range(1, n_lines + 1):
        s = f.readline()
        #print "s: ", s
        i_blank = len(s) - 1
        #print "init i_blank: ", i_blank
        n_flips = 1
        curr_sign = '-'

        #find i_blank
        is_done = False
        while s[i_blank] != '-':
            i_blank -= 1
            #print 'i_blank: ', i_blank
            if i_blank == 0 and s[0] != '-':
                write_output(g, n_case, 0)
                is_done = True
                break
        if is_done:
            continue

        while i_blank >= 0:
            if s[i_blank] != curr_sign:
                n_flips += 1
                curr_sign = s[i_blank]
            i_blank -= 1
        write_output(g, n_case, n_flips)

    f.close()
    g.close()

#n_flips("pancakes_in.txt", "pancakes_out.txt")
#n_flips("B-small-attempt0.in", "pancakes_out0")
n_flips("B-large.in", "B-large-out.txt")