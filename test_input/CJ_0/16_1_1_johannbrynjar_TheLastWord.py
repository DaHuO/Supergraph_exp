if __name__ == "__main__":
    try:
        numberOfCase = int(raw_input(''))
        for i in xrange(numberOfCase):
            S = raw_input('')
            output = '';
            for s in S:
                if output == '':
                    output = s;
                elif s >= output[0]:
                    output = s + output
                else:
                    output = output + s
            print 'Case #{0}: {1}'.format(i+1, output)
    except (EOFError):
        print ''

